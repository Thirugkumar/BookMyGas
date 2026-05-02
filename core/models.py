from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class Cylinder(models.Model):
    CYLINDER_TYPES = [
        ('5KG', '5 Kg'),
        ('14.2KG', '14.2 Kg'),
        ('19KG', '19 Kg'),
    ]
    
    GAS_BRANDS = [
        ('Litro', 'Litro'),
        ('Laugfs', 'Laugfs'),
        ('Other', 'Other'),
    ]

    supplier_name = models.CharField(max_length=255)
    gas_brand = models.CharField(max_length=50, choices=GAS_BRANDS, default='Other')
    cylinder_type = models.CharField(max_length=20, choices=CYLINDER_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    stock_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.supplier_name} - {self.cylinder_type}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Delivered', 'Delivered'),
    ]

    DELIVERY_CHOICES = [
        ('Delivery', 'Home Delivery'),
        ('Pickup', 'Store Pickup'),
    ]

    PAYMENT_CHOICES = [
        ('Card', 'Card Payment'),
        ('COD', 'Cash on Delivery'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    cylinder = models.ForeignKey(Cylinder, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    # Wizard Fields
    delivery_date = models.DateField(null=True, blank=True)
    delivery_time = models.TimeField(null=True, blank=True)
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default='Pickup')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='COD')
    delivery_address = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)

    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.user.username} - {self.status}"
