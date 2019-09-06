from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from django.urls import path, re_path, include


import paint.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('cv/', paint.views.cv),
    path('statement/', paint.views.statement),
    path('contact/', paint.views.contact),
    path('works/', paint.views.techniques),
    path('publications/', paint.views.publications),
    path('', paint.views.home),
]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
