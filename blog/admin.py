from django.contrib import admin
from blog.models import Post, Comment, PostCategory, PostFeedback
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(PostFeedback)
# Register your models here.
