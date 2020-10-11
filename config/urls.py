"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/v1', include(('sunnysouth.users.urls', 'users'), namespace='users')),
    path('api/v1', include(('sunnysouth.sales.urls', 'sales'), namespace='sales'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
