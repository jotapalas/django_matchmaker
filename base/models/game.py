import uuid
from django.db import models


class Game(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    short_name = models.CharField(max_length=3, blank=False, unique=True)

    def __str__(self):
        return f'{self.short_name} - {self.name}'

    def save(self, *args, **kwargs):
        self.short_name = self.short_name.upper()
        super(Game, self).save(*args, **kwargs)
