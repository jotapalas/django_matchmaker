from django.urls import path

from ..views import GameList, GameDetail

urlpatterns = [
    path('', GameList.as_view()),
    path('<str:pk>', GameDetail.as_view()),
]
