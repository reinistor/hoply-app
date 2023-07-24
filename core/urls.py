from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signup',views.signup, name='index'),
    path('signin', views.signin, name='signin'),
    path('upload', views.upload, name='upload'),
    #path('like-post', views.like_post, name='like-post'),
    path('logout', views.logout, name='logout'),
    #path('profile/<str:pk>', views.profile, name='profile'),
    
]
