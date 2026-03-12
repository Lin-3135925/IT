from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "price", "status", "category", "image_url"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }