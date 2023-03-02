from django.contrib import admin
from .models import Author, Post,Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("title", "date","tags", "author",)
    list_display = ("title","date", "author",)
    prepopulated_fields = {"slug": ("title",)}


class AuthoAdmin(admin.ModelAdmin):
       list_filter = ("first_name",)

class CommentAdmin(admin.ModelAdmin):
     list_filter = ("user_name",)



admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthoAdmin)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)