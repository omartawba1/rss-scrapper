from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls')),
    path('accounts/', include('accounts.urls')),
    path('rss/', include('scrappers.urls')),
    path('admin/', admin.site.urls),
]
