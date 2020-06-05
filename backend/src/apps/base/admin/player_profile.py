from django.contrib import admin

from apps.base.models import PlayerProfile


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
