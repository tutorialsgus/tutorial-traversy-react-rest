from django.contrib import admin
from django.urls import path, include # include permite adicionar arquivos externos

urlpatterns = [
    path('', include('leads.urls')), # criar um urls.py dentro do 
]
