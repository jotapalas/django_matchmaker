from rest_framework import serializers
from apps.base.models import Match


class MatchSerializer(serializers.ModelSerializer):
    game = serializers.RelatedField(read_only=True)
    created_by = serializers.RelatedField(read_only=True)

    class Meta:
        model = Match
        fields = [
            'uuid',
            'game',
            'created_by',
            'name',
            'start_date',
            'end_date',
            'short_name',
            'tournament',
            'contenders',
        ]
