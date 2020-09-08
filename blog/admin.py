from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author')
    list_filter = ('author',)
    search_fields = ['title', 'content', 'author__username']  # don't filter on a foreignkey, or just add a __fieldname!


admin.site.register(Post, PostAdmin)