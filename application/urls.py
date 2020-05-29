
from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView,PostCreateView, PostDeleteView, postsearchview
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('post-home', PostListView.as_view(), name='post-home'),
    path('post-home', postsearchview.as_view(), name='post-home'),
    path('product/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('product/new', PostCreateView.as_view(), name='post-create'),
    path('product/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('product/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
