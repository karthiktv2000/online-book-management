from django.contrib import admin
from .models import userModel, booksModel
# Register your models here.

admin.site.register(userModel)

admin.site.register(booksModel)