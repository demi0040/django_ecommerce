from django.contrib import admin
from .models import Carpet, CarpetReview, CarpetImage

class CarpetImageInline(admin.TabularInline):
    model = CarpetImage
    extra = 1

@admin.register(Carpet)
class CarpetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'material', 'size', 'color', 'pattern', 'pile_height', 'origin', 'brand', 'stock_quantity', 'is_active', 'created_at', 'updated_at')
    list_filter = ('material', 'color', 'pattern', 'pile_height', 'origin', 'brand', 'is_active')
    search_fields = ('name', 'description', 'size', 'color', 'pattern', 'pile_height', 'origin', 'brand')
    list_editable = ('price', 'stock_quantity', 'is_active')
    inlines = [CarpetImageInline]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CarpetReview)
class CarpetReviewAdmin(admin.ModelAdmin):
    list_display = ('carpet', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('carpet__name', 'user__username', 'comment')

@admin.register(CarpetImage)
class CarpetImageAdmin(admin.ModelAdmin):
    list_display = ('carpet', 'description')
    search_fields = ('carpet__name', 'description')
