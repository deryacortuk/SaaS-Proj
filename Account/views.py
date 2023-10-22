from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .token import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.views.decorators.cache import never_cache
from django.contrib import messages
import logging
from django.contrib.auth import REDIRECT_FIELD_NAME

logger = logging.getLogger(__name__)

def index(request):
    if request.user.is_authenticated:
        return render(request, "userhub/dashboard.html")
    return render(request,"index.html")



def sing_up(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        to_email = request.POST.get("email")
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
            current_site = get_current_site(request).domain
            subject = "X website Activation Your Account"
            
            message = render_to_string('account/activation/activation_account_email.html',{
                "user":user, "domain":current_site, "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                "token":account_activation_token.make_token(user)
            })
            
            send_mail(subject, message,"sellorbuy@sellorbuy.shop",[to_email], fail_silently=False)
            
            return render(request,"account/activation/activation_email_sent.html",{"user":user})
        else:
            return render(request, "account/signup.html",{"form":form})
    return render(request, "account/signup.html",{"form":form})


def activate(request, uidb64, token, backend="django.contrib.auth.backends.ModelBackend"):
    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
        
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        return render(request, "account/activation/activation_email_success.html")
    return render(request,"account/activation/activation_email_invalid.html")

def user_login(request):
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    logger.info(REDIRECT_FIELD_NAME)
                    login(request, user)
                    return redirect("account:home")
                else:
                    messages.info(request,"Please activate your account.Activation mail was sent.")
            else:
                messages.info(request,"Please check your information!")
    return render(request, "account/login.html",{"form":form})

@never_cache
def user_logout(request):
    logout(request)
    return redirect("account:home")