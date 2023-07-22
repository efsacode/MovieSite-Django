from django.urls import path
from . import views

urlpatterns = [ #burasi bir liste
   path("", views.home), 
   path("home", views.home), 
   path("movies", views.movies), 
    
     
]
