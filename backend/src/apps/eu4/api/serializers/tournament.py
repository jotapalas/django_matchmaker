from rest_framework import serializers
from apps.eu4.models import EU4Tournament


class EU4TournamentSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = EU4Tournament
        fields = [
            'uuid',
            'created_by',
            'name',
            'start_date',
            'end_date',
            'short_name',
        ]
