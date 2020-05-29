
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [


    path('recruiter', recruiter, name='recruiter'),
    path('recruiter-home', recruitersearchview.as_view(), name='recruiter-home'),
    #path('event-home', eventPostListView.as_view(), name='event-home'),
    path('recruiter/<slug:slug>/', recruiterPostDetailView.as_view(), name='recruiter-post-detail'),
    path('recruiters/new/', recruiterPostCreateView.as_view(), name='recruiter-post-create'),
    path('recruiter/<slug:slug>/update/', recruiterPostUpdateView.as_view(), name='recruiter-post-update'),
    path('recruiter/<slug:slug>/delete/', recruiterPostDeleteView.as_view(), name='recruiter-post-delete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

