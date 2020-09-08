from django.shortcuts import render
from django.http import HttpResponse

# DUMMY DATA:

# posts = [
#     {
#         'author': 'Max Z',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'May 11, 2020'
#     },
# {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'May 12, 2020'
#     }
# ]
#
# # Create your views here.
#
#
# def home(request):
#     context = {
#         'posts': posts
#     }
#     # return HttpResponse('<h1>Blog Home</h1>')
#     return render(request, 'blog/home.html', context)  # it still return the HttpResponse in the background
#     # as a third arg, we pass context to the home.html so that we can use 'posts' key with posts values there
#     # like posts.title and etc
#
#
# def about(request):
#     # return HttpResponse('<h1>Blog About</h1>')
#     return render(request, 'blog/about.html', {'title': 'About'})  # instead of passing context, if it's short
#     # we can pass a dictionary directly (title of the page)


# REAL DATA:

from .models import Post  # from models package (in our current dir .) import class Post


# Create your views here.


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     # return HttpResponse('<h1>Blog Home</h1>')
#     return render(request, 'blog/home.html', context)  # it still return the HttpResponse in the background
#     # as a third arg, we pass context to the home.html so that we can use 'posts' key with posts values there
#     # like posts.title and etc


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})  # instead of passing context, if it's short
    # we can pass a dictionary directly (title of the page)


""" --------------- CLASS-BASED VIEWS -----------------"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# instead of home() function above:
class PostListView(ListView):
    # what model to query in order to create the list (in this case - Post, since we want a posts list):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html, blog/post_list.html
    context_object_name = 'posts'
    # ordering = ['date_posted']  # oldest to oldest
    ordering = ['-date_posted']  # latest to oldest
    paginate_by = 5


class UserPostListView(ListView):
    # what model to query in order to create the list (in this case - Post, since we want a posts list):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html, blog/post_list.html
    context_object_name = 'posts'
    # ordering = ['date_posted']  # oldest to oldest
    paginate_by = 5

    # in order to modify the query set  (by default Post model's returning queryset is:
    # queryset = Post.objects.all()) that this list view returns, we can override a method called get_queryset():
    def get_queryset(self):
        # we want to get the user associated with the username that we get from the URL (.../user/Max for e.g.)
        # if that user doesn't exist in the DB, a 404 error will be returned
        # get user from User model with the username(now get username from URL)=self.kwargs(query parameters).get('username'(from the URL))
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        # so returning that filtered post query and our get_queryset method is what will limit our posts on a page for
        # that specific user that has its username as a parameter in URL

# detailed view of the post:
class PostDetailView(DetailView):
    # what model to query in order to create the list (in this case - Post, since we want a posts list):
    model = Post
    # <app>/<model>_<viewtype>.html, blog/post_detail.html

# a view with a form where we create a new post, so we only need to provide the fields that we want to be in that form.
# we want title and content, date posted will be set automatically, and we need to set author
class PostCreateView(LoginRequiredMixin, CreateView):
    # what model to query in order to create the list (in this case - Post, since we want a posts list):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # success_url = path to home page if we want to be redirected to home page
    # success_url = '/'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # what model to query in order to create the list (in this case - Post, since we want a posts list):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # now we want to get the exact post that we're updating using a method of UpdateView called get_object:
        post = self.get_object()  # post we're currently trying to update
        # check if the current user if the author of the post:
        if self.request.user == post.author:
            return True
        return False  # else


# delete post:
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # what model to query in order to create the list (in this case - Post, since we want a posts list):
    model = Post

    def test_func(self):
        # now we want to get the exact post that we're updating using a method of UpdateView called get_object:
        post = self.get_object()  # post we're currently trying to update
        # check if the current user is the author of the post:
        if self.request.user == post.author:
            return True
        return False  # else

    success_url = '/'


