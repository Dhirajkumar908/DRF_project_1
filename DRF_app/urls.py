from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('post/', views.getallpost, name='getallpost'),
    path('createPost', views.createPost, name='createPost'),
    path('delete', views.delete, name='delete'),
    path('get_post', views.get_post,name='get_post'),
    path('updatePost', views.updatePost, name='updatePost')

]