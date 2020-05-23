from django.db import models

from base.models import PlayerProfile, BaseCompetition, BaseContender


class Tournament(BaseCompetition):
    short_name = models.CharField(max_length=5, blank=True)
    contenders = models.ManyToManyField(PlayerProfile, related_name='tournaments', through='TournamentContender')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.game.short_name} {self.start_date.strftime('%Y%m%d')}"
            self.short_name = f"{self.game.short_name}{self.start_date.month}"
        if not self.short_name:
            self.short_name = ''.join([word[0] for word in self.name.split(' ')][:5]).upper()
        super(Tournament, self).save(*args, *kwargs)


class TournamentContender(BaseContender):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
