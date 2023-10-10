from django.db import models


# Create your models here.
class PostCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField()
    isDraft = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Category')

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author = models.ForeignKey('auth.USER', on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Published Date')

    def __str__(self):
        return f"{self.text}"


class PostFeedback(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.USER', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='Text')
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Published Date')
    rating = models.PositiveIntegerField(default=3, verbose_name='Rating')

    def __str__(self):
        return f"{self.text}"
