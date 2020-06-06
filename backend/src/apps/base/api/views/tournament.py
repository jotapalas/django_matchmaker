from rest_framework import generics

from apps.base.models import Tournament
from ..serializers import TournamentSerializer


class TournamentList(generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TournamentDetail(generics.RetrieveUpdateAPIView):
    permission_classes = []  # TODO
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
