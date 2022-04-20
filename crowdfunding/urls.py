from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.addProducts),
    path('edit/<id>', views.editProducts),
    path('delete/', views.deleteProducts)
]