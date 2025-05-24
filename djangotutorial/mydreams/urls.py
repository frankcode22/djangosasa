from django.urls import path

from . import views

app_name = "mydreams"

urlpatterns = [
   
    path("", views.index, name="index"),
    
]