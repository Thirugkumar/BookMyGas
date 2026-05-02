# BookMyGas - Project Status & Features

## 1. Project Overview
**BookMyGas** is a modern Gas Cylinder Find & Booking System built using Python, Django, SQLite, and Bootstrap 5. 

The project has been architected to separate the **Public Portal** (for customers) and the **Admin Portal** (for staff/management) into two distinct, independently runnable projects (`gas_booking` and `gas_admin`), while sharing the same underlying database and `core` app logic.

## 2. Current Status
The project is currently **functional and correctly configured** with its core features implemented. The user interface has been modernized with a premium dark/light glassmorphism theme, dynamic animations, and responsive design.

### Project Structure
- `core/`: The shared Django app containing all models (CustomUser, Cylinder, Booking), views, and forms.
- `gas_booking/`: The main entry point for the public-facing application (run via `manage.py`).
- `gas_admin/`: The administrative entry point for staff (run via `manage_admin.py`).
- `templates/`: Contains all HTML templates separated by `core/` and `registration/`, inheriting from a unified `base.html` that ensures design consistency.
- `static/css/style.css`: Houses the custom CSS variables and styling for the glassmorphic aesthetic.

## 3. Implemented Features

### 👤 Public Portal (Customer Facing)
Accessible via `python manage.py runserver 8000`.

*   **User Authentication**: Custom user registration and secure login/logout.
*   **Store / Find Cylinders**: A dedicated page (`/store`) where users can view available cylinders.
*   **Advanced Filtering**: Users can search and filter the cylinder inventory by:
    *   Supplier Name
    *   Location
    *   Cylinder Type (5 Kg, 14.2 Kg, 19 Kg)
    *   Availability Status
*   **Booking System**: Users can book available cylinders directly from the store.
*   **My List (Dashboard)**: A personalized view where users can track their booking history and current status (Pending, Approved, Rejected, Delivered).

### 🛡️ Admin Portal (Staff Facing)
Accessible via `python manage_admin.py runserver 8001` (Restricted to `is_staff` users).

*   **Admin Dashboard**: Provides a high-level statistical overview:
    *   Total Users
    *   Total Cylinders in Inventory
    *   Total Bookings
    *   Pending Bookings requiring action
*   **Inventory Management**: Full CRUD (Create, Read, Update, Delete) capabilities for Gas Cylinders. Admins can manage supplier details, pricing, stock availability, and location.
*   **Booking Management**: Admins can view all incoming bookings from customers and update their status (e.g., from *Pending* to *Approved* or *Delivered*).

## 4. Technical Stack & Design System
*   **Backend**: Django (Python), SQLite Database.
*   **Frontend**: HTML5, Vanilla JavaScript, Bootstrap 5.
*   **Design Aesthetic**: 
    *   *Glassmorphism*: Semi-transparent backgrounds with backdrop blur.
    *   *Color Palette*: Teal primary (`#008080`), cyan accents (`#00e6e6`), clean white cards, and light teal backgrounds.
    *   *Typography*: Inter font family.
    *   *Responsiveness*: Fully mobile-first design using Bootstrap grid systems.

## 5. Security Measures Implemented
*   **Role-Based Access Control (RBAC)**: `user_passes_test` decorators ensure only admins can access the admin dashboard and management views.
*   **User Isolation**: Customers can only view their own bookings using `request.user` filtering.
*   **CSRF Protection**: All forms utilize Django's `{% csrf_token %}`.
*   **Authentication**: Secure password hashing via Django's `AbstractUser`.
