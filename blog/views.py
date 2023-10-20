from datetime import datetime

from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment, PostCategory, PostFeedback
from blog.forms import PostForm


# Posts
def post_list(request):
    posts = Post.objects.all().filter(isDraft=False)
    count = posts.count()
    categories = PostCategory.objects.all()
    context = {'posts': posts, 'categories': categories, 'count': count}
    return render(request, 'blog/post_list.html', context)

def my_post_list(request):
    posts = Post.objects.filter(author=request.user)
    count = posts.count()
    categories = PostCategory.objects.all()
    context = {'posts': posts, 'categories': categories, 'count': count}
    return render(request, 'blog/my_post_list.html', context)


def post_by_rating(request):
    posts = Post.objects.values('title', 'text', 'author', 'pk').annotate(Avg('post_feedbacks__rating')).order_by(
        '-post_feedbacks__rating__avg')[:5]
    count = posts.count()
    categories = PostCategory.objects.all()
    context = {'posts': posts, 'categories': categories, 'count': count}
    return render(request, 'blog/post_list.html', context)


def post_feedback(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post_feedbacks = PostFeedback.objects.filter(post_id=post_pk)
    context = {'post': post, 'feedbacks': post_feedbacks}
    return render(request, 'blog/post_feedback.html', context)


def post_by_category(request, category_pk):
    posts = Post.objects.filter(category=category_pk)
    categories = PostCategory.objects.all()
    count = posts.count()
    context = {'posts': posts, 'categories': categories, 'count': count}
    return render(request, 'blog/post_list.html', context)


def post_categories(request):
    categories = PostCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/post_list.html', context)


def post_list_draft(request):
    posts = Post.objects.all().filter(isDraft=True)
    categories = PostCategory.objects.all()
    count = posts.count()
    context = {'posts': posts, 'categories': categories, 'count': count}
    return render(request, 'blog/post_list.html', context)


def post_publish(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.isDraft = False
    post.save()
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = Comment.objects.filter(post_id=post_pk)
    comments_count = comments.count()
    context = {'post': post, 'comments': comments, 'comments_count': comments_count}
    return render(request, 'blog/post_detail.html', context)


def post_new(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = datetime.now()
            post.published_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = datetime.now()
            post.published_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_remove(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect('post_list')

# Comments
