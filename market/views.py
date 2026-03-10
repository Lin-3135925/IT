from django.shortcuts import render

# Browse page (temporary minimal version)
def browse(request):
    context = {
        "categories": [],
        "selected_category": request.GET.get("category", ""),
        "q": request.GET.get("q", ""),
        "listings": [],
    }
    return render(request, "market/browse.html", context)

# AJAX partial for listings
def browse_partial(request):
    category = request.GET.get("category")
    q = request.GET.get("q")

    listings = []

    if category:
        pass

    if q:
        pass

    return render(
        request,
        "market/listing_cards.html",
        {"listings": listings}
    )