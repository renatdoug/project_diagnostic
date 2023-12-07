from django.urls import path
from diagnostics.views import entrar, my_csand



urlpatterns = [
    path("", my_csand), 
    path("entrar/", entrar),
      
]