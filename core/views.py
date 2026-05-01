from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Cylinder, Booking

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    cylinder_type = request.GET.get('type', '')
    availability = request.GET.get('availability', '')

    cylinders = Cylinder.objects.all()

    if query:
        cylinders = cylinders.filter(supplier_name__icontains=query)
    if location:
        cylinders = cylinders.filter(location__icontains=location)
    if cylinder_type:
        cylinders = cylinders.filter(cylinder_type=cylinder_type)
    if availability:
        is_avail = True if availability == 'True' else False
        cylinders = cylinders.filter(is_available=is_avail)

    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')

    context = {
        'cylinders': cylinders,
        'user_bookings': user_bookings,
        'types': Cylinder.CYLINDER_TYPES,
        'locations': Cylinder.objects.values_list('location', flat=True).distinct(),
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def book_cylinder(request, cylinder_id):
    cylinder = get_object_or_404(Cylinder, id=cylinder_id)
    if not cylinder.is_available:
        messages.error(request, 'This cylinder is currently out of stock.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        Booking.objects.create(user=request.user, cylinder=cylinder, status='Pending')
        messages.success(request, 'Booking successful! Wait for admin approval.')
        return redirect('dashboard')
    
    return render(request, 'core/book_confirm.html', {'cylinder': cylinder})
