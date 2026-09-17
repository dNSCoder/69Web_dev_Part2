from django.urls import path
from . import views

urlpatterns = [
    path("tailwind_components", views.components_view, name="tailwind_showcase"),
    path("alpineJS_vs_VanillaJS", views.javascripts_view.as_view(), name="javascript_showcase"),
    path("htmx_showcase", views.htmx_demo_view, name='htmx_showcase'),
    path("htmx_showcase/items/add", views.htmx_item_add_view, name='htmx_showcase_add'),
    path("htmx_showcase/items/<int:pk>/delete", views.htmx_item_delete_view, name='htmx_showcase_delete'),
]