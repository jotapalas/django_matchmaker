from django.contrib import admin

from apps.base.models import Tournament, TournamentContender


class ContenderInline(admin.StackedInline):
    model = Tournament.contenders.through


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    model = Tournament
    fields = (
        'game',
        'name',
        'short_name',
        'start_date',
        'end_date',
        'created_by',
    )
    inlines = (
        ContenderInline,
    )
    list_display = ('name', 'short_name', 'game', 'start_date', 'end_date', 'created_by')
