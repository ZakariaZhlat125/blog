from django.urls import path
from . import views

urlpatterns = [
   
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post_detail'),
    path('post/<int:pk>/delete/',views.PostDelete.as_view(),name='article_delete'),
    path('post/<int:pk>/edit/',views.PostUpdate.as_view(),name='article_update'),
    path('post/new/',views.PostCreate.as_view(),name='article_create'),
    path('',views.PostList.as_view(),name='home'),
]
