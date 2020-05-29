
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('services', services, name='services'),
    path('policy', policy, name='privacy-policy'),
    path('about', about, name='about-us'),
    path('terms', terms, name='terms-conditions'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
