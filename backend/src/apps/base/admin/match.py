from django.contrib import admin

from apps.base.models import Match, MatchContender


class ContenderInline(admin.StackedInline):
    model = Match.contenders.through


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    model = Match
    fields = (
        'tournament',
        'game',
        'name',
        'start_date',
        'end_date',
        'created_by'
    )
    inlines = (
        ContenderInline,
    )
    list_display = ('name', 'game', 'tournament', 'start_date', 'end_date')
