from rest_framework import serializers
from apps.base.models import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    game = serializers.RelatedField(read_only=True)
    created_by = serializers.RelatedField(read_only=True)

    class Meta:
        model = Tournament
        fields = [
            'game',
            'created_by',
            'name',
            'start_date',
            'end_date',
            'short_name',
            'contenders',
        ]
