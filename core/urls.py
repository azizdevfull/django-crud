from django.contrib import admin
from django.urls import path, include
from .views import home, create, edit, update
urlpatterns = [
    path('', home),
    path('create/',create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
]
