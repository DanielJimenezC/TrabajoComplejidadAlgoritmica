from django.urls import path
from . import views

urlpatterns = [
     path('', views.Dashboard, name="Dashboard"),
     path('Map', views.Map, name="Map")
]
