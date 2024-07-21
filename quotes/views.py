from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
from .models import Anime, Character, Quote, Favorite
from django.db.models import Exists, OuterRef

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)            
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'quotes/register.html', {'form': form})

    return render(request, 'quotes/register.html', {'form': form})


def login_user(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)           
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    context = {}
    return render(request, 'quotes/login.html', context)


def logout_user(request):
    logout(request)    
    return redirect('login')


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
    character_name = Character.objects.get(id=character_id).name
    favorite_subquery = Favorite.objects.filter(
        user_id=request.user.id, quote_id=OuterRef("pk"))
    quotes = Quote.objects.annotate(favorited=Exists(favorite_subquery))
    print(quotes)
    template = loader.get_template("quotes/quotes.html")
    context = {
        "quotes": quotes,
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


@login_required
def favorite(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    user = request.user
    favorite, created = Favorite.objects.get_or_create(user=user, quote=quote)

    if not created:
        favorite.delete()

    referer_url = request.META.get('HTTP_REFERER', '/')
    return redirect(referer_url)


@login_required
def get_favorites(request):
    favorites = Favorite.objects.all().filter(user_id=request.user.id)
    template = loader.get_template("quotes/favorites.html")
    context = {
        "favorites": favorites
    }
    return HttpResponse(template.render(context, request))
