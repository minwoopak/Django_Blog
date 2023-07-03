from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context=context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # default is object_list
    ordering = ['-date_posted']  # newest to oldest
    paginate_by = 5  # 5 posts per page


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # default is object_list
    paginate_by = 5  # 5 posts per page

    def get_queryset(self): # override default queryset
        # get user object
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return all posts by user
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # success_url = '/'  # redirect to home page after successful post creation

    def form_valid(self, form):
        # set author to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # success_url = '/'  # redirect to home page after successful post creation

    def form_valid(self, form):
        # set author to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # get current post
        post = self.get_object()
        # check if current user is author of post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # redirect to home page after successful post deletion

    def test_func(self):
        # get current post
        post = self.get_object()
        # check if current user is author of post
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})