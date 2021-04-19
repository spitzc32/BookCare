"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('admin/', admin.site.urls),
    path('accounts/', include('app.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password/reset/', auth_views.PasswordResetView.as_view(), {'template_name':'registration/password_change.html'}, name='password_reset'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(), {'template_name':'registration/password_change_done.html'}, name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(), {'template_name' : 'registration/forgot_password.html'}, name='password_reset_confirm'),
    path('api/', include('app.apiv1.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]
