from django.urls import path

from ..views import MatchList, MatchDetail

urlpatterns = [
    path('', MatchList.as_view()),
    path('<str:pk>', MatchDetail.as_view()),
]
