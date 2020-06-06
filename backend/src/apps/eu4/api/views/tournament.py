from rest_framework import generics

from apps.eu4.models import EU4Tournament
from ..serializers import EU4TournamentSerializer


class EU4TournamentList(generics.ListCreateAPIView):
    queryset = EU4Tournament.objects.all()
    serializer_class = EU4TournamentSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EU4TournamentDetail(generics.RetrieveUpdateAPIView):
    permission_classes = []  # TODO
    queryset = EU4Tournament.objects.all()
    serializer_class = EU4TournamentSerializer
