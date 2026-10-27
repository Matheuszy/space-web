from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static as statics


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
] + statics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

