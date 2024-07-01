from django.contrib import admin

# Register your models here.
from .models import Carpet

@admin.register(Carpet)
class CarpetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'material', 'size', 'color', 'pattern', 'pile_height', 'origin', 'brand', 'stock_quantity', 'is_active', 'created_at', 'updated_at')
    list_filter = ('material', 'color', 'pattern', 'pile_height', 'origin', 'brand', 'is_active')
    search_fields = ('name', 'description', 'size', 'color', 'pattern', 'pile_height', 'origin', 'brand')
    list_editable = ('price', 'stock_quantity', 'is_active')