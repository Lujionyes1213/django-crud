# Create your views here.


from django.views.generic import ListView,  DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    
class PostCreateView(CreateView):
    model = Post
    fields = ['_all_']
    success_url = reverse_lazy('blog:all')
        

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['_all_'] 
    success_url = reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
    model = Post
    fields = ['_all_']
    success_url = reverse_lazy('blog:all')

    template_name = 'post_confirm_delete.html'