from django.urls import path, include

from ..views import EU4CountryList, EU4CountryDetail

urlpatterns = [
    path('', EU4CountryList.as_view()),
    path('<int:pk>', EU4CountryDetail.as_view())
]
