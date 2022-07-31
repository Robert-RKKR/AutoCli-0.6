# Django Import:
from django.urls import path, include
from django.contrib import admin

# Admin URL pattern:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
]
