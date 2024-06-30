from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path("", views.index_anime, name="home"),
    path("<int:anime_id>/", views.index_anime_characters,
         name="index all characters"),
    path("character/<int:character_id>/",
         views.index_character_quotes, name="index all quotes"),
    path("quote/<int:quote_id>/",
         views.get_quote, name="get one quote"),
     
]
