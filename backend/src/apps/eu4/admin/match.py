from django.contrib import admin

from apps.eu4.models import EU4Match


class EU4MatchContenderInline(admin.StackedInline):
    model = EU4Match.contenders.through


@admin.register(EU4Match)
class EU4MatchAdmin(admin.ModelAdmin):
    model = EU4Match
    fields = (
        'tournament',
        'start_date',
        'end_date',
        'created_by'
    )
    inlines = (
        EU4MatchContenderInline,
    )
    list_display = ('name', 'game', 'tournament', 'start_date', 'end_date')
