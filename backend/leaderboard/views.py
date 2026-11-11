from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Game, Player, Score
from .serializers import GameSerializer, PlayerSerializer, ScoreSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # GET /api/games/{id}/scores/ - all scores of one game
    @action(detail=True, methods=["get"])
    def scores(self, request, pk=None):
        game = self.get_object()  # 404 if the game does not exist
        return Response(ScoreSerializer(game.scores.all(), many=True).data)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    # GET /api/players/{id}/scores/ - all scores of one player
    @action(detail=True, methods=["get"])
    def scores(self, request, pk=None):
        player = self.get_object()  # 404 if the player does not exist
        return Response(ScoreSerializer(player.scores.all(), many=True).data)


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
