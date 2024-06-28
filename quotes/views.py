from django.template import loader
from django.http import HttpResponse
from .models import Anime, Character, Quote

# Create your views here.


def index_anime(request):
    all_anime = Anime.objects.all()
    template = loader.get_template("quotes/index.html")
    context = {
        "anime": all_anime
    }
    return HttpResponse(template.render(context, request))


def index_anime_characters(request, anime_id):
    all_characters = Character.objects.all().filter(anime_id=anime_id)
    anime_name = Anime.objects.get(id=anime_id).name
    template = loader.get_template("quotes/characters.html")
    context = {
        "characters": all_characters,
        "anime_name": anime_name
    }
    return HttpResponse(template.render(context, request))


def index_character_quotes(request, character_id):
    all_quotes = Quote.objects.all().filter(character_id=character_id)
    character_name = Character.objects.get(id=character_id).name
    template = loader.get_template("quotes/quotes.html")
    context = {
        "quotes": all_quotes,
        "character_name": character_name
    }
    return HttpResponse(template.render(context, request))


def get_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    template = loader.get_template("quotes/quote.html")
    context = {
        "quote": quote
    }
    return HttpResponse(template.render(context, request))
