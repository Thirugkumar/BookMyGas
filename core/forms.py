from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Cylinder, Booking

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone_number')

class CylinderForm(forms.ModelForm):
    class Meta:
        model = Cylinder
        fields = ['supplier_name', 'cylinder_type', 'price', 'location', 'is_available', 'stock_quantity']
        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cylinder_type': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
