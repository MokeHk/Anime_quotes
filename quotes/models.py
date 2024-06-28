from django.db import models

# Create your models here.
# animes table
class Anime(models.Model):
    name = models.CharField(max_length=200)
    pic_url = models.CharField(max_length=500)

# characters table
class Character(models.Model):
    name = models.CharField(max_length=100)
    pic_url = models.CharField(max_length=500)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

# quotes table
class Quote(models.Model):
    text = models.CharField(max_length=500)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)