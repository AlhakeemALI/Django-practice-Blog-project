from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils.text import slugify
from django.core import validators
from django.urls import reverse


# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Post(models.Model):
    title= models.CharField(max_length=150)
    excerpt = models.CharField(max_length=1000)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug= models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)


def get_absolute_url(self):
    return reverse("post-detail", args=[self.slug])

def save(self, *args, **kwargs):
     self.slug = slugify(self.title)
     super().save(*args, **kwargs)

def __str__(self):
    return f"{self.tile} "

