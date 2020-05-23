from django.db import models

from base.models import BaseCompetition, BaseContender, PlayerProfile
from base.factories import GameFactory

from eu4.models import EU4Country


class EU4Tournament(BaseCompetition):
    short_name = models.CharField(max_length=5, blank=True)
    contenders = models.ManyToManyField(PlayerProfile, related_name='eu4_tournaments', through='EU4TournamentContender')

    class Meta:
        verbose_name = "tournament"
        verbose_name_plural = "tournaments"

    def __init__(self, *args, **kwargs):
        super(EU4Tournament, self).__init__(*args, **kwargs)
        self.game = GameFactory(short_name='EU4')


class EU4TournamentContender(BaseContender):
    tournament = models.ForeignKey(EU4Tournament, on_delete=models.PROTECT)
    preferred_tier = models.IntegerField(choices=EU4Country.Tier.choices[1:], verbose_name='Preferred tier')
    country = models.ForeignKey(EU4Country, on_delete=models.PROTECT, blank=True, null=True, related_name='tournaments')
