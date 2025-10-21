from django.urls import path
from . import views


urlpatterns = [
    # homepage
    path('', views.home, name='home'),
]