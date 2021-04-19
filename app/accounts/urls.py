from django.urls import path

from .views import SignUpView, HomeView


urlpatterns = [
	path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
]