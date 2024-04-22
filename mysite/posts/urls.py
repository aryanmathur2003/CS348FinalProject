from django.urls import path
from .views import *

urlpatterns = [
    # User URLs
    path('user/add/', AddUser.as_view(), name='add_user'),
    path('user/edit/<str:username_in>/', EditUser.as_view(), name='edit_user'),
    path('user/delete/<str:username_in>/', DeleteUser.as_view(), name='delete_user'),
    path('user/posts/<str:username_in>/', UserPosts.as_view(), name='user_posts'),

    # Post URLs
    path('post/add/', AddPost.as_view(), name='add_post'),
    path('post/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),

    # Comment URLs

    path('comment/add/', AddComment.as_view(), name='add_comment'),

    # Reports URLs

    path('report/add/', AddReport.as_view(), name='add_report'),

] 