from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    STATUS_CHOICES = [
        ("AVAILABLE", "Available"),
        ("SOLD", "Sold"),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="AVAILABLE")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="listings")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    image_url = models.URLField(blank=True)