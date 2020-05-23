from django.db import models


class EU4Country(models.Model):
    class Tier(models.IntegerChoices):
        UNPLAYABLE = 0
        DIAMOND = 1
        GOLD = 2
        SILVER = 3
        BRONZE = 4

    name = models.CharField(max_length=100, blank=False)
    tag = models.CharField(max_length=3, db_index=True)
    tier = models.IntegerField(choices=Tier.choices, blank=False, default=Tier.UNPLAYABLE)
    exists_in_1444 = models.BooleanField(default=True)
    is_formable = models.BooleanField(default=False)
    is_releasable = models.BooleanField(default=False)
    is_revolter = models.BooleanField(default=False)
    is_colonial_nation = models.BooleanField(default=False)
    is_special_country = models.BooleanField(default=False, help_text='Spawned with console or from CK converter.')
    appears_by_event = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return f'{self.name} ({self.tag})'
