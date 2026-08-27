from django.urls import path
from . import views

urlpatterns = [
    path("/tailwind_components", views.components_view, name="tailwind_showcase"),
]