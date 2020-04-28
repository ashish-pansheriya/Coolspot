
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import friendPostListView,friendPostDetailView,friendPostCreateView,friendPostUpdateView,friendPostDeleteView, filter


urlpatterns = [

    path('stuff', filter, name='stuff'),
    path('friend-home', friendPostListView.as_view(), name='friend-home'),
    path('friend/<int:pk>/', friendPostDetailView.as_view(), name='friend-post-detail'),
    path('friend/new/', friendPostCreateView.as_view(), name='friend-post-create'),
    path('friend/<int:pk>/update/', friendPostUpdateView.as_view(), name='friend-post-update'),
    path('friend/<int:pk>/delete/', friendPostDeleteView.as_view(), name='friend-post-delete'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

