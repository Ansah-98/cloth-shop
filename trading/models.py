
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    location = models.CharField(max_length=200,)
    number = models.CharField(max_length=14)
    bio = models.CharField(max_length=200)

class Product(models.Model):
    by = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    type_of = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now = True)
    posted = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(default= 'cart.png' )

    def __str__(self):
        return self.name 
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    posted = models.DateTimeField(auto_now =True)