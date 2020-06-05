from django.contrib import admin

from apps.eu4.models import EU4Country


@admin.register(EU4Country)
class EU4CountryAdmin(admin.ModelAdmin):
    model = EU4Country
    fields = (
        'name',
        'tag',
        'tier',
        'exists_in_1444',
        'is_formable',
        'is_revolter',
        'is_colonial_nation',
        'is_special_country',
        'appears_by_event'
    )
    list_display = ('name', 'tag', 'tier')
