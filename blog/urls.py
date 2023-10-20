from django.urls import path

from blog.views import post_list, post_detail, post_new, post_edit, post_remove, post_list_draft, post_publish, \
    post_by_category, post_feedback, post_by_rating, my_post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('posts/my_posts', my_post_list, name='my_post_list'),
    path('posts/rating', post_by_rating, name='post_by_rating'),
    path('post/detail/feedback/<int:post_pk>', post_feedback, name='post_feedback'),
    path('post/draft', post_list_draft, name='post_draft'),
    path('post/category/<int:category_pk>', post_by_category, name='post_by_category'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('post/remove/<int:post_pk>', post_remove, name='post_remove'),
    path('post/publish/<int:post_pk>', post_publish, name='post_publish'),
    path('post/new', post_new, name='post_new'),
]
