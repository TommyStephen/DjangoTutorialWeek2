from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

from django.views.generic import ListView
from django.db.models import Q
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # 5 posts per page

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        return Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'body', 'category', 'tags']
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body', 'category', 'tags']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


