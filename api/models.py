from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(User):
    address = models.CharField(max_length=355)
    country_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=20)



class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField("api.Book")

class Book(models.Model):
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=350)
    description = models.TextField(max_length=3500)
    genres = models.ManyToManyField("api.Genres")
    rating = models.IntegerField(default=0)
    pages = models.CharField(max_length=50)

class Genres(models.Model):
    name = models.CharField(max_length=50)

class Cart(models.Model):
    user = models.ForeignKey("api.CustomUser", on_delete=models.CASCADE)
    books = models.ManyToManyField("api.Book")
    price = models.IntegerField(default=0)

class Order(models.Model):
    user = models.ForeignKey("api.CustomUser", on_delete=models.CASCADE)
    library = models.ForeignKey("api.Library", on_delete=models.CASCADE)
    books = models.ManyToManyField("api.Book")
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)