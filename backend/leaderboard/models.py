from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=50)

    class Meta:
        ordering = ["id"]


class Player(models.Model):
    username = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ["id"]


class Score(models.Model):
    # one player has many scores, one game has many scores
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="scores")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="scores")
    points = models.PositiveIntegerField()

    class Meta:
        ordering = ["-points", "id"]  # highest score first
