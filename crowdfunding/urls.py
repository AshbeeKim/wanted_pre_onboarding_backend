from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(f"", views.ProductsList.as_view()),
    path(f"<int:id>/", views.ProductsDetail.as_view()),
    path(f"<int:id>/funding/", views.ProductsFunding.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)