from eu4.models import EU4Tournament, EU4Match
from django.contrib import admin


class EU4ContenderInline(admin.TabularInline):
    model = EU4Tournament.contenders.through


class EU4MatchInline(admin.TabularInline):
    model = EU4Match
    fields = (
        'tournament',
        'start_date',
        'end_date',
        'created_by'
    )


@admin.register(EU4Tournament)
class EU4TournamentAdmin(admin.ModelAdmin):
    model = EU4Tournament
    fields = (
        'name',
        'short_name',
        'start_date',
        'end_date',
        'created_by',
    )
    inlines = (
        EU4ContenderInline,
        EU4MatchInline
    )
    list_display = ('name', 'short_name', 'start_date', 'end_date', 'created_by')
