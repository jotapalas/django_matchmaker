from rest_framework import serializers
from apps.eu4.models import EU4Match, EU4Tournament, EU4MatchContender


class EU4MatchContenderSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = EU4MatchContender
        fields = [
            'player',
            'country',
            'subbing'
        ]


class EU4MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = EU4Match
        fields = [
            'uuid',
            'name',
            'start_date',
            'end_date'
        ]


class EU4MatchSerializerDetail(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    tournament = serializers.PrimaryKeyRelatedField(read_only=False, queryset=EU4Tournament.objects.all())

    class Meta:
        model = EU4Match
        fields = [
            'uuid',
            'created_by',
            'name',
            'start_date',
            'end_date',
            'tournament',
            'contenders',
            'contenders_detail'
        ]
