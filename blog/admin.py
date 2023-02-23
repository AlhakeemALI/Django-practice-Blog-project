from django.contrib import admin
from .models import Author, Post,Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("title", "date",)
    list_display = ("title",)


class AuthoAdmin(admin.ModelAdmin):
       list_filter = ("first_name",)



admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthoAdmin)
admin.site.register(Tag)