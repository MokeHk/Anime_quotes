from django.db import models

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


# users table
class User(models.Model):
    user_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=80)
    password = models.CharField(max_length=500)


# favorites table
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
