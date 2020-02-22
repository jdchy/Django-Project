from django.urls import path
from .views import NewsP, Home, Contact, Newsdate, Register, addUser, modelform, addModalForm, upload, book_list, upload_book

urlpatterns = [
	path('news/',NewsP,name='News' ),
    path('',Home,name='Home' ),
    path('contact/',Contact,name='Contact'),
    path('newsdate/<int:year>',Newsdate,name='Newsdate'),
    path('register/',Register,name='Register'),
    path('addUser/',addUser,name='addUser'),
    path('modalform/',modelform,name='modelform'),
    path('addmodalform/',addModalForm,name='modalform'),
    path('upload/',upload,name='upload'),
    path('books/',book_list,name='book_list'),
    path('books/upload/',upload_book,name='upload_book'),
]