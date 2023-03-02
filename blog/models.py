from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils.text import slugify
from django.core import validators
from django.urls import reverse


# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Post(models.Model):
    title= models.CharField(max_length=150)
    excerpt = models.CharField(max_length=1000)
    image =models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug= models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tags = models.ManyToManyField(Tag)



class Comment(models.Model):
        user_name = models.CharField(max_length=120)
        user_email = models.EmailField()
        text = models.TextField(max_length=400)
        post = models.ForeignKey(Post , on_delete=models.CASCADE, related_name='comments')


        def __str__(self):
         return f'{self.user_name}'



