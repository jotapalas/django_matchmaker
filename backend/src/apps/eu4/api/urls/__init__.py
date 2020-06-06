from django.urls import path, include

urlpatterns = [
    path(r'country/', include('apps.eu4.api.urls.country'))
]
