from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Carpet(models.Model):
    MATERIAL_CHOICES = [
        ('wool', 'Wool'),
        ('silk', 'Silk'),
        ('synthetic', 'Synthetic'),
        ('cotton', 'Cotton'),
        ('jute', 'Jute'),
        ('viscose', 'Viscose'),
        ('polypropylene', 'Polypropylene'),
        ('polyester', 'Polyester'),
        ('acrylic', 'Acrylic'),
        ('leather', 'Leather'),
        ('natural_fiber', 'Natural Fiber'),
        ('blend', 'Blend'),
    ]
    
    PILE_HEIGHT_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    PATTER_CHOICES = [
        ('oriental', 'Oriental'),
        ('modern', 'Modern'),
        ('floral', 'Floral'),
        ('geometric', 'Geometric'),
        ('solid', 'Solid'),
        ('striped', 'Striped'),
        ('abstract', 'Abstract'),
        ('shag', 'Shag'),
        ('animal_print', 'Animal Print'),
        ('southwestern', 'Southwestern'),
        ('moroccan', 'Moroccan'),
        ('chevron', 'Chevron'),
        ('paisley', 'Paisley'),
        ('damask', 'Damask'),
        ('ikat', 'Ikat'),
        ('trellis', 'Trellis'),
        ('tribal', 'Tribal'),
        ('vintage', 'Vintage'),
        ('bohemian', 'Bohemian'),
        ('coastal', 'Coastal'),
        ('traditional', 'Traditional'),
    ]
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100, choices=MATERIAL_CHOICES)  # e.g., wool, silk, synthetic
    size = models.CharField(max_length=50)  # e.g., "5' x 7'"
    shipping_dimensions = models.CharField(max_length=100, default='200cm x 15cm x 10cm')  # e.g., "200cm x 15cm x 10cm"
    color = models.CharField(max_length=50)
    pattern = models.CharField(max_length=100, choices=PATTER_CHOICES)  # e.g., Oriental, Modern, Floral
    pile_height = models.CharField(max_length=50, choices=PILE_HEIGHT_CHOICES)  # e.g., low, medium, high
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

    class Meta:
        ordering = ('-created_at',)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def average_rating(self):
        return self.reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0
    
    def __str__(self):
        return f"{self.name} - {self.size}"

class CarpetReview(models.Model):
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['carpet', 'user']

    def __str__(self):
        return f"Review for {self.carpet.name} by {self.user.username}"

class CarpetImage(models.Model):
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='carpet_gallery/')
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Image for {self.carpet.name}"
