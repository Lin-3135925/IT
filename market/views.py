from django.shortcuts import render
from .models import Category, Listing
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ListingForm

def browse(request):
    category = request.GET.get("category", "")
    q = request.GET.get("q", "")

    listings = Listing.objects.select_related("category").all().order_by("-created_at")
    categories = Category.objects.all().order_by("name")

    if category:
        listings = listings.filter(category_id=category)

    if q:
        listings = listings.filter(title__icontains=q)

    context = {
        "categories": categories,
        "selected_category": category,
        "q": q,
        "listings": listings,
    }
    return render(request, "market/browse.html", context)

def browse_partial(request):
    category = request.GET.get("category", "")
    q = request.GET.get("q", "")

    listings = Listing.objects.select_related("category").all().order_by("-created_at")

    if category:
        listings = listings.filter(category_id=category)

    if q:
        listings = listings.filter(title__icontains=q)

    return render(request, "market/listing_cards.html", {"listings": listings})

from django.shortcuts import get_object_or_404

def listing_detail(request, listing_id: int):
    listing = get_object_or_404(Listing.objects.select_related("category"), pk=listing_id)
    return render(request, "market/detail.html", {"listing": listing})

@login_required
def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("browse")
    else:
        form = ListingForm()

    return render(request, "market/create.html", {"form": form})