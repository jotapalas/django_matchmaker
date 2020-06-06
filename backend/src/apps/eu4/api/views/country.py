from rest_framework import generics

from apps.eu4.models import EU4Country
from ..serializers import EU4CountrySerializer


class EU4CountryList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all Countries

    post:
    Create a new country
    """
    queryset = EU4Country.objects.all()
    serializer_class = EU4CountrySerializer


class EU4CountryDetail(generics.RetrieveUpdateAPIView):
    """
    get:
    Return a single Country

    put:
    Update an existing Country
    """
    permission_classes = []  # TODO only admins should be able to post, put or delete countries
    queryset = EU4Country.objects.all()
    serializer_class = EU4CountrySerializer
