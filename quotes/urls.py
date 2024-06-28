from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_anime, name="index all anime"),
    path("<int:anime_id>/", views.index_anime_characters,
         name="index all characters"),
    path("character/<int:character_id>/",
         views.index_character_quotes, name="index all quotes"),
    path("quote/<int:quote_id>/",
         views.get_quote, name="get one quote")
]
