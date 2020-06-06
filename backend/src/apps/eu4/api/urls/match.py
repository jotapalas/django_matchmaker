from django.urls import path

from ..views import EU4MatchList, EU4MatchDetail

urlpatterns = [
    path('', EU4MatchList.as_view()),
    path('<str:pk>', EU4MatchDetail.as_view()),
]
