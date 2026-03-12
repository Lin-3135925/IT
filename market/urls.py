from django.urls import path
from . import views

urlpatterns = [
    path("browse/", views.browse, name="browse"),
    path("browse/partial/", views.browse_partial, name="browse_partial"),
    path("listing/<int:listing_id>/", views.listing_detail, name="listing_detail"),
    path("listing/create/", views.listing_create, name="listing_create"),
]