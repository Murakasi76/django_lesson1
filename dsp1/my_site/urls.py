from django.urls import path
from my_site import views

urlpatterns = [
    path("index/", views.index, name="index"),
]
