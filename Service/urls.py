from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Account.urls",namespace="account")),
    path("q/",include("UserHub.urls", namespace="userhub")),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
