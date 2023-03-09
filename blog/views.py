
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView
from . forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.


class StartingPageView(ListView):
      template_name = "blog/index.html"
      model = Post
      ordering = ["-date"]
      context_object_name = "posts"
      def get_queryset(self):
        queryset =  super().get_queryset()
        date = queryset[:3]
        return date
   
class AllPostView(ListView):
       template_name = "blog/all-posts.html"
       model = Post
       ordering = ["-date"]
       context_object_name = "all_posts"

class PostDetailView(View):
      template_name =  "blog/post-ditail.html"
      model = Post
      context_object_name = "singel_post"

      def get(self,request,slug):
          post= Post.objects.get(slug=slug)
          context = {
               "post": post,
               "tags": post.tags.all(),
               "comment_form": CommentForm()
            
          }
          return render(request, "blog/post-ditail.html", context)
         
      def post(self,request,slug):
         comment_form = CommentForm(request.POST)
         post= Post.objects.get(slug=slug)
         if comment_form.is_valid():
             comment = comment_form.save(commit=False) 
             comment.post = post
             comment.save()
             return HttpResponseRedirect(reverse("post-detail", args=[slug]))
         post= Post.objects.get(slug=slug)
         context = {
               "post": post,
               "tags": post.tags.all(),
               "comment_form": CommentForm()
         }
         return render(request, "blog/post-ditail.html", context)
         




    

    

 



