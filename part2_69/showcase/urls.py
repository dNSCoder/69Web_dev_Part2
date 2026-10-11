from django.urls import path
from . import views

urlpatterns = [
    path("/tailwind_components", views.components_view, name="tailwind_showcase"),
    path("htmx-demo/", views.htmx_demo_view, name="htmx_demo"),
    path("htmx-demo/items/add/", views.demo_item_add_view, name="demo_item_add"),
    path("htmx-demo/search/", views.demo_search_view, name="demo_search"),
    path("htmx-demo/items/<int:pk>/delete/", views.demo_item_delete_view, name="demo_item_delete"),
]
