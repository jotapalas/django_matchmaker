from rest_framework import generics

from apps.base.models import Tournament
from ..serializers import TournamentSerializer


class TournamentList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all Tournaments

    post:
    Create a new tournament
    """
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentDetail(generics.RetrieveUpdateAPIView):
    """
    get:
    Return a single Tournament

    put:
    Update an existing Tournament
    """
    permission_classes = []  # TODO only admins should be able to post, put or delete
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
