from rest_framework import serializers
from apps.eu4.models import EU4Match, EU4Tournament


class EU4MatchSerializer(serializers.ModelSerializer):
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
            'tournament'
        ]
