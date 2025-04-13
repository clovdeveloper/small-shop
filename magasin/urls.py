from django.contrib import admin
from django.urls import path

from shop import views
from shop.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
path('', home, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:pk>/update/', views.article_update, name='article_update'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),

    path('commandes/', views.commande_list, name='commande_list'),
    path('commandes/create/', views.commande_create, name='commande_create'),
    path('commandes/<int:pk>/update/', views.commande_update, name='commande_update'),
    path('commandes/<int:pk>/delete/', views.commande_delete, name='commande_delete'),

    path('ventes/', views.vente_list, name='vente_list'),
    path('ventes/create/', views.vente_create, name='vente_create'),
    path('ventes/<int:pk>/update/', views.vente_update, name='vente_update'),
    path('ventes/<int:pk>/delete/', views.vente_delete, name='vente_delete'),

    path('fournisseurs/', views.fournisseur_list, name='fournisseur_list'),
    path('fournisseurs/create/', views.fournisseur_create, name='fournisseur_create'),
    path('fournisseurs/<int:pk>/update/', views.fournisseur_update, name='fournisseur_update'),
    path('fournisseurs/<int:pk>/delete/', views.fournisseur_delete, name='fournisseur_delete'),

    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/update/', views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),

    path('categories/', views.categorie_list, name='categorie_list'),
    path('categories/create/', views.categorie_create, name='categorie_create'),
    path('categories/<int:pk>/update/', views.categorie_update, name='categorie_update'),
    path('categories/<int:pk>/delete/', views.categorie_delete, name='categorie_delete'),

    path('employes/', views.employe_list, name='employe_list'),
    path('employes/create/', views.employe_create, name='employe_create'),
    path('employes/<int:pk>/update/', views.employe_update, name='employe_update'),
    path('employes/<int:pk>/delete/', views.employe_delete, name='employe_delete'),
]

