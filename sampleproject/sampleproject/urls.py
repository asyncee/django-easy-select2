from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls.base import reverse_lazy
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notes/', include('demoapp.urls')),
    url(r'', RedirectView.as_view(url=reverse_lazy('note-list')),
        name='frontpage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
