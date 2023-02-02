from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="home_page"),
    path("Riyadh/", views.riyadh, name="Riyadh"),
    path("Jeddah/", views.jeddah, name="Jeddah"),
    path("Taif/", views.taif, name="Taif"),
    path("Ula/", views.ula, name="Ula"),
]