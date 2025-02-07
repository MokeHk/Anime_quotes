from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

# Create your models here.
# animes table


class Anime(models.Model):
    name = models.CharField(max_length=200)
    pic_url = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

# characters table


class Character(models.Model):
    name = models.CharField(max_length=100)
    pic_url = models.CharField(max_length=500)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# quotes table


class Quote(models.Model):
    text = models.CharField(max_length=500)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text


# favorites table
class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
