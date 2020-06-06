from django.urls import path, include

urlpatterns = [
    path('', include('rest_framework.urls')),
    path(r'tournament/', include('apps.base.api.urls.tournament')),
    path(r'game/', include('apps.base.api.urls.game')),

    # OTHER APPS
    path(r'eu4/', include('apps.eu4.api.urls'))
]
