from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home') # one empty path to indicate that this is the route URL.
]