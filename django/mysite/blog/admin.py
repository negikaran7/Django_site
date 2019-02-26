from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models


class PostAdmin(admin.ModelAdmin):
    # fields=[
    #     "title",
    #     "date_posted",
    #     "content",
    #   "author"
    # ]
    fieldsets = [
        ("Title", {"fields": ["title"]}),
        ("Date&Time", {"fields": ["date_posted"]}),
        ("Content", {"fields": ["content"]}),
        ("author", {"fields": ["author"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Post,PostAdmin)
