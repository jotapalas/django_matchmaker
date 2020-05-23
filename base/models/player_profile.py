import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class PlayerProfile(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=100, blank=False, unique=True)
    register_date = models.DateTimeField(default=now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        if self.nickname is None:
            self.nickname = self.user.username

        super(PlayerProfile, self).save(*args, **kwargs)
