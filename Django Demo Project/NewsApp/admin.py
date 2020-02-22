from django.contrib import admin
from .models import News, SportNews, RegistrationData, Book
# Register your models here.

admin.site.register(News)
admin.site.register(SportNews)
admin.site.register(RegistrationData)
admin.site.register(Book)
