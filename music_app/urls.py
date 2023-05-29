from django.urls import path

from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('upload/', views.upload_music, name='upload_music'),
    path('', views.homepage, name='homepage'),
]