from django.urls import path
from . import views
from .views import ReviewsForm

urlpatterns = [
    path('', views.index),
    path('feedback', views.feedback),
    path('post_feedback/', views.post_feedback),
    path('login', views.login),
    path('add_user', views.add_user),
    path('add_devices', views.add_devices),
    path('map_PGU', views.map_PGU),
    path('indexforpolsovatel', views.indexforpolsovatel)
]