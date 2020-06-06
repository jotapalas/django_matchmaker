from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('', admin.site.urls),
    path('api/', include('apps.base.api.urls'))
]
