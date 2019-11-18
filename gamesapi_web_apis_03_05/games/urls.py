"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import path
from games import views

urlpatterns = [
    path('games/', views.GameList.as_view(),
         name=views.GameList.name),
    path('games/<int:pk>/', views.GameDetail.as_view(),
         name=views.GameDetail.name),
    path('game-categories/', views.GameCategoryList.as_view(),
         name=views.GameCategoryList.name),
    path('game-categories/<int:pk>/', views.GameCategoryDetail.as_view(),
         name=views.GameCategoryDetail.name),
    path('players/', views.PlayerList.as_view(),
         name=views.PlayerList.name),
    path('players/<int:pk>/', views.PlayerDetail.as_view(),
         name=views.PlayerDetail.name),
    path('scores/', views.ScoreList.as_view(),
         name=views.ScoreList.name),
    path('scores/<int:pk>/', views.ScoreDetail.as_view(),
         name=views.ScoreDetail.name),
    path('users/', views.UserList.as_view(),
         name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(),
         name=views.UserDetail.name),

    path('', views.ApiRoot.as_view(),
         name=views.ApiRoot.name),

]
