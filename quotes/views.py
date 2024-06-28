from django.http import HttpResponse

# Create your views here.
def index_anime(request):
    return HttpResponse("Here lies all anime")

def index_anime_characters(request, anime_id):
    return HttpResponse("Here lies all character in this anime")

def index_character_quotes(request, anime_id, character_id):
    return HttpResponse("Here lies all quotes from this character")

def get_quote(request, anime_id, character_id, quote_id):
    return HttpResponse("Here lies a quote")