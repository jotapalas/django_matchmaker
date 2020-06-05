import factory

from apps.base.models import Game


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game
        django_get_or_create = ('short_name', )

    name = 'Example Game'
