
from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('post-home', PostListView.as_view(), name='post-home'),
#    path('', home, name='home'),
    path('', blogsearchview.as_view(), name='home'),
#    path('blog-home', blogsearchview.as_view(), name='blog-home'),
    path('blog/<slug:slug>/', blogDetailView.as_view(), name='blog-detail'),
    path('blogs/new/', blogCreateView.as_view(), name='blog-create'),
    path('blog/<slug:slug>/update/', blogUpdateView.as_view(), name='blog-update'),
    path('blog/<slug:slug>/delete/', blogDeleteView.as_view(), name='blog-delete'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
