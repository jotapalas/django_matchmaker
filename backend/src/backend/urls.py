from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('', admin.site.urls),

    # REST API
    path(r'api/', include('apps.base.api.urls')),
    path(r'api/eu4/', include('apps.eu4.api.urls'))
]
