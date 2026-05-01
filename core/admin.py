from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cylinder, Booking

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )

@admin.register(Cylinder)
class CylinderAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'cylinder_type', 'price', 'location', 'is_available')
    list_filter = ('cylinder_type', 'is_available', 'location')
    search_fields = ('supplier_name', 'location')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cylinder', 'status', 'booking_date')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'cylinder__supplier_name')
    actions = ['approve_bookings', 'reject_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(status='Approved')
    approve_bookings.short_description = "Approve selected bookings"

    def reject_bookings(self, request, queryset):
        queryset.update(status='Rejected')
    reject_bookings.short_description = "Reject selected bookings"

admin.site.register(CustomUser, CustomUserAdmin)
