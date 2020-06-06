from django.urls import path, include

urlpatterns = [
    path('', include('rest_framework.urls')),
    path(r'game/', include('apps.base.api.urls.game')),
    path(r'tournament/', include('apps.base.api.urls.tournament')),
    path(r'match/', include('apps.base.api.urls.match')),
]
