from django.urls import path
from .views import  instagram_discovery, analyze_user

app_name = "userhub"

urlpatterns = [
    path("", instagram_discovery, name="discovery"),
    path("<username>/", analyze_user, name="analysis"),
]
