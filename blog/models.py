from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# This file contains a series of classes that Django's ORM converts to database tables.
# An ORM is a program that allows you to create classes that correspond to database tables.
# Class attributes correspond to columns, and instances of the classes correspond to rows in the database.
# When using ORM, the classes you build that represent database tables are referred as models.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now=True)  # when posted
    # date_posted = models.DateTimeField(auto_now_add=True)  # when created
    date_posted = models.DateTimeField(default=timezone.now)  # when created
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key automatically means Many-to-One
    # that is many posts can be created by only one user

    # dunder str method:
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse will return the full path of the post-detail route as a string,
        # compared to redirect that just redirects
        return reverse('post-detail', kwargs={'pk': self.pk})  # it needs a specific post with a primary key,
        # URL parameter is 'pk' with a value of self.pk (instance of the specific post pk).
