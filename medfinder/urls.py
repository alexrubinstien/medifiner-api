from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static

from medications.api_urls_v1 import medications_api_urlpatterns
from public.api_urls_v1 import public_api_urlpatterns

api_urlpatterns = [

    path('accounts/', include('rest_registration.api.urls')),
    path('medications/', include(medications_api_urlpatterns)),
    path('public/', include(public_api_urlpatterns)),
]


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

"""
URL settings for debug_toolbar if instaled.
"""

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
