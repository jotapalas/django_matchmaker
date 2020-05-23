import uuid
from django.db import models

from base.models import Game, PlayerProfile


class BaseCompetition(models.Model):
    """
    Abstract class for match and tournament.
    """
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True, primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(PlayerProfile, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class BaseContender(models.Model):
    player = models.ForeignKey(PlayerProfile, on_delete=models.PROTECT)

    class Meta:
        abstract = True
