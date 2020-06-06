from django.urls import path

from ..views import TournamentList, TournamentDetail

urlpatterns = [
    path('', TournamentList.as_view()),
    path('<int:pk>', TournamentDetail.as_view()),

]
