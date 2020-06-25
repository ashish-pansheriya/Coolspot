from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
#friendPostListView,friendPostDetailView,friendPostCreateView,friendPostUpdateView,friendPostDeleteView, filter,Searchview



urlpatterns = [
   # path('friend',ProgressBarUploadView.as_view(), name='friend-post-create'),
  #  path('form', geter, name='form'),
    path('stuff', filter, name='stuff'),
    path('Friends', Searchview.as_view(), name='friend-home'),
#    path('friend-home', friendPostListView.as_view(), name='friend-home'),
    path('friends/<slug:slug>/', friendPostDetailView.as_view(), name='friend-post-detail'),
    path('friend/new/', friendPostCreateView.as_view(), name='friend-post-create'),
    path('friend/<slug:slug>/update/', friendPostUpdateView.as_view(), name='friend-post-update'),
    path('friend/<slug:slug>/delete/', friendPostDeleteView.as_view(), name='friend-post-delete'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

