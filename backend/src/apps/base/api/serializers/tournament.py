from django.contrib.auth.models import User
from rest_framework import serializers
from apps.base.models import Tournament, Game, TournamentContender


class TournamentSerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Game.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tournament
        fields = [
            'uuid',
            'game',
            'created_by',
            'name',
            'start_date',
            'end_date',
            'short_name',
        ]
