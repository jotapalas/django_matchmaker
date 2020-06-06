from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

from apps.base.models import BaseCompetition, BaseContender, PlayerProfile
from apps.base.factories import GameFactory

from apps.eu4.models import EU4Country


class EU4Tournament(BaseCompetition):
    short_name = models.CharField(max_length=5, blank=True)
    contenders = models.ManyToManyField(PlayerProfile, related_name='eu4_tournaments', through='EU4TournamentContender')
    schedule = JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = "tournament"
        verbose_name_plural = "tournaments"

    def __init__(self, *args, **kwargs):
        super(EU4Tournament, self).__init__(*args, **kwargs)
        self.game = GameFactory(short_name='EU4')

    def __str__(self):
        short_name = f' ({self.short_name})' if self.short_name else ''
        return f'{self.name}{short_name}'


class EU4TournamentContender(BaseContender):
    tournament = models.ForeignKey(EU4Tournament, on_delete=models.PROTECT)
    preferred_tier = models.IntegerField(choices=EU4Country.Tier.choices[1:], verbose_name='Preferred tier')
    preferred_countries = ArrayField(base_field=models.CharField(max_length=4, blank=True), default=list, blank=True)
    country = models.ForeignKey(EU4Country, on_delete=models.PROTECT, blank=True, null=True, related_name='tournaments')

    def __str__(self):
        return f"{str(self.player)}: {str(self.country)}"
