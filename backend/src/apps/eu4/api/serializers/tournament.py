from rest_framework import serializers
from apps.eu4.models import EU4Tournament, EU4TournamentContender
from apps.eu4.api.serializers import EU4MatchSerializer


class EU4TournamentContenderSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = EU4TournamentContender
        fields = [
            'player',
            'preferred_tier',
            'preferred_countries',
            'country'
        ]


class EU4TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EU4Tournament
        fields = [
            'uuid',
            'name',
            'short_name',
        ]


class EU4TournamentSerializerDetail(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    contenders_detail = EU4TournamentContenderSerializer(many=True)
    matches = EU4MatchSerializer(many=True)

    class Meta:
        model = EU4Tournament
        fields = [
            'uuid',
            'created_by',
            'name',
            'start_date',
            'end_date',
            'short_name',
            'contenders',
            'contenders_detail',
            'matches'
        ]

