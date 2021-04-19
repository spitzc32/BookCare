from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import Account

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@method_decorator([login_required], name='dispatch')
class HomeView(generic.View):
    model = Account
    template_name = "dashboard/home.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return redirect('home') #needs defined as valid url
        return super(HomeView, self).dispatch(request, *args, **kwargs)
