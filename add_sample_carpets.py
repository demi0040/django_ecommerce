import os
import django
import uuid
from django.core.files import File
from django.utils.text import slugify
from pathlib import Path

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_project.settings")
django.setup()

from store.models import Carpet

def generate_unique_slug(name, model):
    slug = slugify(name)
    unique_slug = slug
    num = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{slug}-{num}'
        num += 1
    return unique_slug

def add_sample_carpets():
    carpets = [
        {
            'name': 'Persian Silk',
            'description': 'Luxurious Persian silk carpet with intricate designs.',
            'price': 999.99,
            'material': 'silk',
            'size': '6\' x 9\'',
            'color': 'Red and Gold',
            'pattern': 'oriental',
            'pile_height': 'low',
            'origin': 'Iran',
            'stock_quantity': 5,
            'image_name': 'persian_silk.png'
        },
        {
            'name': 'Modern Geometric',
            'description': 'Contemporary carpet with bold geometric patterns.',
            'price': 599.99,
            'material': 'wool',
            'size': '5\' x 7\'',
            'color': 'Gray and White',
            'pattern': 'geometric',
            'pile_height': 'medium',
            'origin': 'USA',
            'stock_quantity': 10,
            'image_name': 'modern_geometric.png'
        },
    ]

    for carpet_data in carpets:
        image_name = carpet_data.pop('image_name')
        try:
            carpet, created = Carpet.objects.update_or_create(
                name=carpet_data['name'],
                defaults=carpet_data
            )
            carpet.slug = generate_unique_slug(carpet.name, Carpet)
            carpet.sku = carpet.sku or str(uuid.uuid4())[:8].upper()
            
            image_path = Path(__file__).resolve().parent / 'sample_images' / image_name
            if image_path.exists():
                with open(image_path, 'rb') as f:
                    carpet.featured_image.save(image_name, File(f), save=True)
            
            print(f"{'Created' if created else 'Updated'} carpet: {carpet.name}")
        except Exception as e:
            print(f"Error processing carpet {carpet_data['name']}: {str(e)}")

    print("Sample carpet creation/update process completed.")

if __name__ == "__main__":
    add_sample_carpets()