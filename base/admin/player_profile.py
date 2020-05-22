from base.models import PlayerProfile
from django.contrib import admin


@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    model = PlayerProfile
    fields = (
        'user',
        'nickname',
        'register_date',
        'active',
    )
    list_display = ('nickname', 'register_date', 'active')