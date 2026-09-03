from django.urls import path
from . import views

urlpatterns = [
    path("/tailwind_components", views.components_view, name="tailwind_showcase"),
    path("/alpineJS_vs_VanillaJS", views.javascripts_view.as_view(), name="javascript_showcase"),
]