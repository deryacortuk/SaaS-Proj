from django.urls import path
from .views import sing_up, user_login, user_logout, activate, index

app_name = "account"

urlpatterns = [
    path("", index, name="home"), 
    path("signup/", sing_up, name="signup"), 
    path("login/", user_login, name="login"), 
    path("logout/", user_logout, name="logout"), 
    path("activate/<uidb64>/<token>/", activate, name="activate"), 
    
    
]