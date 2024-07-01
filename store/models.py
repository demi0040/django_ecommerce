from django.db import models

class Carpet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)  # e.g., wool, silk, synthetic
    size = models.CharField(max_length=50)  # e.g., "5' x 7'", "200cm x 300cm"
    color = models.CharField(max_length=50)
    pattern = models.CharField(max_length=100)  # e.g., Oriental, Modern, Floral
    pile_height = models.CharField(max_length=50)  # e.g., low, medium, high
    origin = models.CharField(max_length=100)  # Country or region of origin
    brand = models.CharField(max_length=100, blank=True, null=True)
    stock_quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.size}"