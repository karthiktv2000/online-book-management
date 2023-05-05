from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.

class userModel(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True, editable=False)
    location = models.CharField(max_length=20, blank=True)
    shop_name = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super(userModel, self).save(*args, **kwargs)


class booksModel(models.Model):
    user = models.ForeignKey(userModel, on_delete=models.CASCADE, related_name='books')
    book_name = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    number_of_copies = models.IntegerField()        