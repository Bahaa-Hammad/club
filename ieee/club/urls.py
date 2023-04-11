from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('landing_page.urls')),
    path('event/', include('events.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
