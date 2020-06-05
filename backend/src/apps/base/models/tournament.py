from django.db import models

from apps.base.models import PlayerProfile, BaseCompetition, BaseContender


class Tournament(BaseCompetition):
    short_name = models.CharField(max_length=5, blank=True)
    contenders = models.ManyToManyField(PlayerProfile, related_name='tournaments', through='TournamentContender')

    def __str__(self):
        return self.name


class TournamentContender(BaseContender):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
