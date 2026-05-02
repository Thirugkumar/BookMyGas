from core.models import Cylinder

def update_brands():
    cylinders = Cylinder.objects.all()
    for cylinder in cylinders:
        name = cylinder.supplier_name.lower()
        if 'litro' in name:
            cylinder.gas_brand = 'Litro'
        elif 'lauf' in name or 'laugf' in name:
            cylinder.gas_brand = 'Laugfs'
        else:
            cylinder.gas_brand = 'Other'
        cylinder.save()
    print("Gas brands updated successfully.")

update_brands()
