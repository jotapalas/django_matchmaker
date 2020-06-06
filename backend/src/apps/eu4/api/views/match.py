from rest_framework import generics

from apps.eu4.models import EU4Match
from ..serializers import EU4MatchSerializer


class EU4MatchList(generics.ListCreateAPIView):
    queryset = EU4Match.objects.all()
    serializer_class = EU4MatchSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EU4MatchDetail(generics.RetrieveUpdateAPIView):
    permission_classes = []  # TODO
    queryset = EU4Match.objects.all()
    serializer_class = EU4MatchSerializer
