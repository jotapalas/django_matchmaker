from rest_framework import generics

from apps.base.models import Game
from ..serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateAPIView):
    permission_classes = []  # TODO
    queryset = Game.objects.all()
    serializer_class = GameSerializer
