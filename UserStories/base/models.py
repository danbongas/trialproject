from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

#from django.contrib.auth.models import User

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []



class Recipe(models.Model):
    #name = 
    #description =  
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    servings = models.IntegerField(null=True, blank=True)
    preparationTime = models.TimeField(null=True, blank=True)
    foodart = models.ImageField(null=True, blank=True, upload_to='images/')
    ingredients = RichTextField(null=True, blank=True)
    instructions =  RichTextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-updated', '-created']
        

    def __str__(self):
        return self.name
    

    
# class Instructions(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)   
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
    

#     def __stry__(self):
#         return self.body[0:50]