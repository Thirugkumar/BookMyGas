import os
import django
import json

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gas_booking.settings')
django.setup()

from core.models import Cylinder

def import_data():
    with open('jaffna_gas_distributors.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    for item in data:
        supplier = item['store_name']
        address = item['address']
        phone = item['phone_number']
        
        # Append phone number to location if available
        if phone != "Not Available":
            location_str = f"{address} (Tel: {phone})"
        else:
            location_str = address

        # Check if already exists to avoid duplicates if run multiple times
        if not Cylinder.objects.filter(supplier_name=supplier, location=location_str).exists():
            # Create a default 14.2KG cylinder listing for each distributor
            Cylinder.objects.create(
                supplier_name=supplier,
                cylinder_type='14.2KG',
                price=3985.00,  # Approximate current price in LKR
                location=location_str,
                is_available=True
            )
            count += 1
            
    print(f"Successfully imported {count} new gas cylinder listings into the database.")

if __name__ == '__main__':
    import_data()
