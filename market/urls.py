from django.urls import path
from . import views

urlpatterns = [
    path("browse/", views.browse, name="browse"),
    path("browse/partial/", views.browse_partial, name="browse_partial"),
]