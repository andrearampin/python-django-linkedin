from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^social/', include('social_network_interface.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
