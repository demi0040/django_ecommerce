from django.db import models
from django.contrib.auth.models import User

class Carpet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)  # e.g., wool, silk, synthetic
    size = models.CharField(max_length=50)  # e.g., "5' x 7'"
    shipping_dimensions = models.CharField(max_length=100, default='200cm x 15cm x 10cm')  # e.g., "200cm x 15cm x 10cm"
    color = models.CharField(max_length=50)
    pattern = models.CharField(max_length=100)  # e.g., Oriental, Modern, Floral
    pile_height = models.CharField(max_length=50)  # e.g., low, medium, high
    origin = models.CharField(max_length=100)  # Country or region of origin
    brand = models.CharField(max_length=100, blank=True, null=True)
    stock_quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sku = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # in kilograms
    care_instructions = models.TextField(null=True, blank=True)
    shipping_info = models.TextField(null=True, blank=True)
    warranty_info = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(upload_to='carpet_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.size}"

class CarpetReview(models.Model):
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.carpet.name} by {self.user.username}"

class CarpetImage(models.Model):
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='carpet_gallery/')
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Image for {self.carpet.name}"
