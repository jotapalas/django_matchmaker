from rest_framework import serializers
from apps.eu4.models import EU4Country


class EU4CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EU4Country
        fields = [
            'name',
            'tag',
            'tier',
            'exists_in_1444',
            'is_formable',
            'is_releasable',
            'is_revolter',
            'is_colonial_nation',
            'is_special_country',
            'appears_by_event'
        ]
