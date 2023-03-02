
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView



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
        return context


    

    

      # if we want to get limte data we can use this method
      #  def get_queryset(self):
      #      queryest =  super().get_queryset()
      #      date = queryest
      #      return date



# def starting_page(request):
#   latest_posts =  Post.objects.all().order_by("-date")[:3]
#   return render(request, "blog/index.html", {
#     "posts": latest_posts
#   })

# def posts(request):
#  all_posts = Post.objects.all().order_by("-date")
#  return render(request, "blog/all-posts.html", {
#   "all_posts": all_posts
#  })

# def post_detail(request, slug):
#   # identified_post = Post.objects.get(slug=slug)
#   identified_post = get_object_or_404(Post,slug=slug)
#   return render(request, "blog/post-ditail.html", {
#     "singel_post": identified_post,
#     "tags" : identified_post.tags.all()
#   })