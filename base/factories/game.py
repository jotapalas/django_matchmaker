import factory

from base.models import Game


class GameFactory(factory.Factory):
    class Meta:
        model = Game
        django_get_or_create = ('short_name', )

    name = 'Example Game'
