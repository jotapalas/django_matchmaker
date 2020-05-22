from base.models import Game
from django.contrib import admin


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game
    fields = (
        'name',
        'short_name',
    )
    list_display = ('name', 'short_name')
