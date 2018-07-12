from django.conf.urls import include
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('rooms/', include('rooms.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/rooms/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
