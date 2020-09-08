from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    # let's create a path to our blog's homepage:
    # the url path for our blog home page mapped to our home function in the views file
    # path('', views.home, name='blog-home'),  # '' means homepage,
    path('', PostListView.as_view(), name='blog-home'),  # '' means homepage,
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # then we are specifying the view that we want to handle the logic at that homepage route,
    # and we want that to be our homeview from our views module
    # also we specify name for this path to use in base.html for a href
    # views.home is the function that we created in the views module
    # that just returns that HttpResponse
    path('about/', views.about, name='blog-about')
]