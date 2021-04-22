from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import Post

class PostList(ListView):
    queryset=Post.objects.filter(status=1).order_by('-created_on')
    template_name='index.html'
class PostDetail(DetailView):
    model=Post
    template_name='post_detail.html'
class PostDelete(DeleteView):
    model=Post
    template_name='article_delete.html'
    success_url='/'
class PostCreate(CreateView):
    model=Post
    templatename='article_create.html'
    fields='__all__'
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdate(UpdateView):
    model=Post
    template_name='article_update.html'
    fields=['title','slug','content','status']