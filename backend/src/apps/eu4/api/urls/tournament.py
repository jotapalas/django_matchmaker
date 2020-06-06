from django.urls import path

from ..views import EU4TournamentList, EU4TournamentDetail

urlpatterns = [
    path('', EU4TournamentList.as_view()),
    path('<str:pk>', EU4TournamentDetail.as_view()),
]
