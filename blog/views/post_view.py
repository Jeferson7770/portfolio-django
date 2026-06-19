from django.views import generic
from blog.models.post import Post


class PostView(generic.ListView):

    queryset = Post.objects.all().order_by("-created_at")
    template_name = "index.html"
    context_object_name = "post_list"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
