from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView
from django.contrib import messages
from .forms import CustomUserCreationForm, CylinderForm, BookingStatusForm
from .models import CustomUser, Cylinder, Booking
from .ai_service import ai_rank_cylinders

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def store(request):
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    cylinder_type = request.GET.get('type', '')
    availability = request.GET.get('availability', '')
    gas_brand = request.GET.get('brand', '')

    cylinders = Cylinder.objects.all()

    if query:
        cylinders = cylinders.filter(supplier_name__icontains=query)
    if location:
        cylinders = cylinders.filter(location__icontains=location)
    if cylinder_type:
        cylinders = cylinders.filter(cylinder_type=cylinder_type)
    if gas_brand:
        cylinders = cylinders.filter(gas_brand=gas_brand)
    if availability:
        is_avail = True if availability == 'True' else False
        cylinders = cylinders.filter(is_available=is_avail)

    cylinders = ai_rank_cylinders(request.user, cylinders)

    # Normalize for reusable component
    formatted_types = [{'value': t[0], 'label': t[1]} for t in Cylinder.CYLINDER_TYPES]
    formatted_brands = [{'value': b[0], 'label': b[1]} for b in Cylinder.GAS_BRANDS]
    
    def format_location_label(loc):
        if loc and '(Tel:' in loc:
            return loc.split('(Tel:')[0].strip()
        return loc
        
    formatted_locations = [{'value': loc, 'label': format_location_label(loc)} for loc in Cylinder.objects.values_list('location', flat=True).distinct()]
    availability_options = [
        {'value': 'True', 'label': 'Available'},
        {'value': 'False', 'label': 'Out of Stock'},
    ]

    context = {
        'cylinders': cylinders,
        'types': formatted_types,
        'brands': formatted_brands,
        'locations': formatted_locations,
        'availability_options': availability_options,
    }
    return render(request, 'core/store.html', context)

@login_required
def my_list(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'core/my_list.html', {'user_bookings': user_bookings})

@login_required
def book_cylinder(request, cylinder_id):
    cylinder = get_object_or_404(Cylinder, id=cylinder_id)
    if not cylinder.is_available:
        messages.error(request, 'This cylinder is currently out of stock.')
        return redirect('store')
    
    if request.method == 'POST':
        delivery_date = request.POST.get('delivery_date')
        delivery_time = request.POST.get('delivery_time')
        delivery_method = request.POST.get('delivery_method')
        payment_method = request.POST.get('payment_method')
        delivery_address = request.POST.get('delivery_address')
        contact_number = request.POST.get('contact_number')

        booking = Booking.objects.create(
            user=request.user, 
            cylinder=cylinder, 
            status='Pending',
            delivery_date=delivery_date,
            delivery_time=delivery_time,
            delivery_method=delivery_method,
            payment_method=payment_method,
            delivery_address=delivery_address,
            contact_number=contact_number
        )
        return render(request, 'core/book_confirm.html', {'cylinder': cylinder, 'success': True, 'booking': booking})
    
    return render(request, 'core/book_confirm.html', {'cylinder': cylinder})

# --- Admin Portal Views ---

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = CustomUser.objects.count()
    total_cylinders = Cylinder.objects.count()
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='Pending').count()
    context = {
        'total_users': total_users,
        'total_cylinders': total_cylinders,
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings
    }
    return render(request, 'core/admin_dashboard.html', context)

@user_passes_test(is_admin)
def admin_inventory(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            cylinder_id = request.POST.get('cylinder_id')
            cylinder = get_object_or_404(Cylinder, id=cylinder_id)
            cylinder.delete()
            messages.success(request, 'Cylinder deleted successfully.')
            return redirect('admin_inventory')
        else:
            cylinder_id = request.POST.get('cylinder_id')
            if cylinder_id:
                cylinder = get_object_or_404(Cylinder, id=cylinder_id)
                form = CylinderForm(request.POST, instance=cylinder)
            else:
                form = CylinderForm(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Cylinder saved successfully.')
                return redirect('admin_inventory')
    else:
        form = CylinderForm()

    cylinders = Cylinder.objects.all().order_by('-created_at')
    return render(request, 'core/admin_cylinders.html', {'cylinders': cylinders, 'form': form})

@user_passes_test(is_admin)
def admin_bookings(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingStatusForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, f'Booking #{booking_id} status updated.')
            return redirect('admin_bookings')
    
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'core/admin_bookings.html', {'bookings': bookings})

@user_passes_test(is_admin)
def admin_customers(request):
    users = CustomUser.objects.filter(is_staff=False).order_by('-date_joined')
    return render(request, 'core/admin_customers.html', {'customers': users})

@user_passes_test(is_admin)
def admin_payments(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'core/admin_payments.html', {'bookings': bookings})

@user_passes_test(is_admin)
def admin_reports(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    payment_method = request.GET.get('payment_method')
    delivery_method = request.GET.get('delivery_method')
    
    if start_date:
        bookings = bookings.filter(booking_date__date__gte=start_date)
    if end_date:
        bookings = bookings.filter(booking_date__date__lte=end_date)
    if payment_method and payment_method != 'all':
        bookings = bookings.filter(payment_method=payment_method)
    if delivery_method and delivery_method != 'all':
        bookings = bookings.filter(delivery_method=delivery_method)
        
    total_bookings = bookings.count()
    total_revenue = sum([b.cylinder.price for b in bookings if b.status in ['Delivered', 'Approved']])
    
    delivery_count = bookings.filter(delivery_method='Delivery').count()
    pickup_count = bookings.filter(delivery_method='Pickup').count()
    
    card_count = bookings.filter(payment_method='Card').count()
    cod_count = bookings.filter(payment_method='COD').count()
    
    context = {
        'total_bookings': total_bookings,
        'total_revenue': total_revenue,
        'delivery_count': delivery_count,
        'pickup_count': pickup_count,
        'card_count': card_count,
        'cod_count': cod_count,
        'bookings': bookings,
    }
    return render(request, 'core/admin_reports.html', context)
