from django.contrib import admin

from apps.base.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game
    fields = (
        'name',
        'short_name',
    )
    list_display = ('name', 'short_name')
