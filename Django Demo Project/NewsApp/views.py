from django.shortcuts import render, redirect
from .models import News,SportNews,RegistrationData, Book 	
from .forms import RegistrationForm, RegistrationModal, BookForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.

def Home(request):
	context = {
		"name": "Joydip Chowdhury",
		"number": '+880183318****'
	}

	return render(request,'home.html',context)

def NewsP(request):
	obj = News.objects.all()

	context = {
		"data":obj
	}
	return render(request,'news.html',context)

def Newsdate(request, year):
	article_list = News.objects.filter(pub_date__year= year)
	context = {
		'year' : year,
		'article_list' : article_list
	}
	return render(request, 'newsdate.html', context)

def Contact(request):
	return render(request,'contact.html')

def Register(request):
	context = {
		"form":RegistrationForm
	}
	return render(request, 'signup.html',context)

def addUser(request):
	form = RegistrationForm(request.POST)
	if form.is_valid():
		myregister = RegistrationData(username = form.cleaned_data['username'],
									password = form.cleaned_data['password'],
									email = form.cleaned_data['email'],
									phone = form.cleaned_data['phone'])
		myregister.save()
		messages.add_message(request,messages.SUCCESS,'You have successfully registered')
	return redirect('Register')

def modelform(request):
	context = {
		"modalform": RegistrationModal
	}
	return render(request, 'modalform.html',context)

def addModalForm(request):
	mymodalform = RegistrationModal(request.POST)
	if mymodalform.is_valid():
		myregister.save()
	return redirect('modelform')

def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name,uploaded_file)
		context['url'] = fs.url(name)
	return render(request, 'upload.html',context)

def book_list(request):
	books = Book.objects.all()
	return render(request, 'book_list.html',{'books':books})

def upload_book(request):
	form = BookForm()
	if request.method == 'POST':
		form = BookForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('book_list')
		else:
			form = BookForm()
	return render(request, 'upload_book.html',{'form':form})