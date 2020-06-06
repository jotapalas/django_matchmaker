from django.urls import path

from ..views import TournamentList, TournamentDetail

urlpatterns = [
    path('', TournamentList.as_view()),
    path('<str:pk>', TournamentDetail.as_view()),
]
