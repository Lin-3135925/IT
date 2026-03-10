from django.urls import path
from . import views

urlpatterns = [
    path("browse/partial/", views.browse_partial, name="browse_partial"),
]