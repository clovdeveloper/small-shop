
from django.urls import path

from magasin.article import views

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:pk>/edit/', views.article_update, name='article_update'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),
]

