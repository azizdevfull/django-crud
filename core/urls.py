from django.contrib import admin
from django.urls import path, include
from .views import home, create
urlpatterns = [
    path('', home),
    path('create/',create, name="create"),
]
