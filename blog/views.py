
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView
from . forms import CommentForm



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

class PostDetailView(DetailView):
    template_name =  "blog/post-ditail.html"
    model = Post
    context_object_name = "singel_post"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context


    

    

 



