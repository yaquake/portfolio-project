from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Blog


class BlogAdmin(SummernoteModelAdmin):
    fields = ['title', 'pub_date', 'image', 'short_description', 'body']
    summernote_fields = ('body', )




admin.site.register(Blog, BlogAdmin)