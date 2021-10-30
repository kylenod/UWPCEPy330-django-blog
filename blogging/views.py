from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    template_name = "blogging/list.html"
    queryset = Post.objects.order_by("-published_date")[:5]


class PostDetailView(DetailView):
    template_name = "blogging/detail.html"
    model = Post

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        context = {"object": post}
        return render(request, "blogging/detail.html", context)
