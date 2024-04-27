from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




# Authentication
class AuthLockScrren(LoginRequiredMixin,TemplateView):
    template_name = "pages/authentication/auth-lock-screen.html"
class AuthLogin(LoginRequiredMixin,TemplateView):
    template_name = "pages/authentication/auth-login.html"
class AuthRegister(LoginRequiredMixin,TemplateView):
    template_name = "pages/authentication/auth-register.html"
class AuthRecoverpw(LoginRequiredMixin,TemplateView):
    template_name = "pages/authentication/auth-recoverpw.html"

# Pages
class Error404(LoginRequiredMixin,TemplateView):
    template_name = "pages/utility/pages-404.html"
class Error500(LoginRequiredMixin,TemplateView):
    template_name = "pages/utility/pages-500.html"
class ComingSoon(LoginRequiredMixin,TemplateView):
    template_name = "pages/utility/pages-comingsoon.html"
class Faqs(LoginRequiredMixin,TemplateView):
    template_name = "pages/utility/pages-faqs.html"
class Maintenance(LoginRequiredMixin,TemplateView):
    template_name = "pages/utility/pages-maintenance.html"
class Pricing(LoginRequiredMixin,TemplateView):
    template_name = "pages/utility/pages-pricing.html"   
class Starter(LoginRequiredMixin,TemplateView):
    template_name = "pages/utility/pages-starter.html"
class Timeline(LoginRequiredMixin,TemplateView):
    template_name = "pages/utility/pages-timeline.html"