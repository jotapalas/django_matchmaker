from rest_framework import generics

from apps.base.models import Match
from ..serializers import MatchSerializer


class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MatchDetail(generics.RetrieveUpdateAPIView):
    permission_classes = []  # TODO
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
