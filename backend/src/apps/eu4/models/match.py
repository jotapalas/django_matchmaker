from django.db import models

from apps.base.models import BaseCompetition, BaseContender, PlayerProfile
from apps.base.factories import GameFactory

from apps.eu4.models import EU4Tournament, EU4Country


class EU4Match(BaseCompetition):
    tournament = models.ForeignKey(EU4Tournament, blank=True, null=True, on_delete=models.SET_NULL, related_name='matches')
    contenders = models.ManyToManyField(PlayerProfile, related_name='eu4_matches',
                                        through='EU4MatchContender', through_fields=('match', 'player'))

    class Meta:
        verbose_name = "match"
        verbose_name_plural = "match"

    def __init__(self, *args, **kwargs):
        super(EU4Match, self).__init__(*args, **kwargs)
        self.game = GameFactory(short_name='EU4')


class EU4MatchContender(BaseContender):
    match = models.ForeignKey(EU4Match, on_delete=models.CASCADE, related_name='contenders_detail')
    country = models.ForeignKey(EU4Country, on_delete=models.PROTECT, related_name='matches')
    subbing = models.ForeignKey(PlayerProfile, on_delete=models.SET_NULL, blank=True, null=True, related_name='subs')

    class Meta:
        verbose_name = 'contender'
        verbose_name_plural = 'contenders'
