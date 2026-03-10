from django.shortcuts import render

# Create your views here.
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