from django.db import models

from base.models import (
    BaseCompetition, BaseContender,
    Tournament, Game, PlayerProfile
)


class Match(BaseCompetition):
    tournament = models.ForeignKey(Tournament, blank=True, null=True, on_delete=models.SET_NULL)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=False)
    contenders = models.ManyToManyField(PlayerProfile, related_name='matches', through='MatchContender')

    class Meta:
        verbose_name_plural = 'matches'

    def save(self, *args, **kwargs):
        if not self.name:
            tournament = self.tournament
            self.name = (tournament.short_name if tournament else self.game.short_name)
            self.name += self.start_date.strftime('%Y%m%d%H%m')

        super(Match, self).save(*args, **kwargs)


class MatchContender(BaseContender):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
