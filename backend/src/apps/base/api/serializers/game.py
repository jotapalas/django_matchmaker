from rest_framework import serializers
from apps.base.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'uuid',
            'name',
            'short_name',
        ]
