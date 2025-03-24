from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    about,
    profile_update,
    like_post,
    like_comment,
    add_comment
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('profile/update/', profile_update, name='profile_update'),
    path('about/', about, name='about'),
    path('post/<int:pk>/like/', like_post, name='like_post'),
    path('comment/<int:pk>/like/', like_comment, name='like_comment'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
]
