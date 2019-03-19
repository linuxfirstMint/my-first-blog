from django.urls import path
from . import views

urlpatterns = [
    # ex: http://127.0.0.1:8000
    path('', views.post_list, name='post_list'),
    # ex: http://127.0.0.1:8000/post/5
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]