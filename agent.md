# Gas Cylinder Find & Booking System - Agent Guidelines & Project Standards

This document serves as the core reference for maintaining project consistency, ensuring security, and preserving the defined UI/UX aesthetics (theme colors, responsiveness) across the entire application. Future development or AI agent interventions must adhere strictly to these guidelines.

---

## 1. Security Standards

The system is built with Django, which provides robust built-in security. All future features must adhere to the following principles:

### Authentication & Authorization
*   **User Isolation:** Ensure users can only view and manage their own bookings. Never query `Booking.objects.all()` without filtering by `request.user` in user-facing views.
*   **Password Management:** Rely strictly on Django’s built-in password hashing algorithms (PBKDF2). Never store plaintext passwords or modify the hashing mechanism directly.
*   **Role-Based Access Control (RBAC):** Restrict inventory management, booking approvals, and user administration to `is_staff` or `is_superuser` accounts via the Django Admin interface.

### Protection Against Common Vulnerabilities
*   **CSRF Protection:** Every POST form in the application must include the `{% csrf_token %}` template tag.
*   **SQL Injection:** Always use the Django ORM to interact with the database. Avoid raw SQL queries (`.raw()`) unless absolutely necessary, and if used, strictly parameterize inputs.
*   **XSS (Cross-Site Scripting):** Rely on Django’s auto-escaping templates. If rendering raw HTML is required in the future, explicitly sanitize the input using libraries like `bleach`.
*   **Environment Variables:** Keep `SECRET_KEY`, database credentials, and any third-party API keys out of version control. (Currently, `SECRET_KEY` is in `settings.py` for development but MUST be moved to a `.env` file for production).

---

## 2. Project Consistency

To keep the codebase maintainable and predictable, follow these structural rules:

### Architecture Pattern (MVT)
*   **Models (`models.py`):** Fat models, skinny views. Keep business logic and data formatting closely tied to the models (e.g., custom model properties).
*   **Views (`views.py`):** Use Function-Based Views (FBVs) or Class-Based Views (CBVs) consistently. Currently, the project uses FBVs with `@login_required` decorators for explicit readability.
*   **Templates:** Inherit from `base.html` for all new pages. Use the `{% block content %}` and `{% block main_class %}` blocks consistently.

### Code Style
*   **Python:** Adhere to PEP 8 standards. Use clear variable names (e.g., `cylinder_type` rather than `ctype`).
*   **Django:** Keep app scopes isolated. If a new major feature is added (e.g., Payments), create a new app (`python manage.py startapp payments`) rather than bloating the `core` app.

---

## 3. UI/UX: Theme Color & Responsiveness

The project utilizes **Bootstrap 5** alongside a custom CSS file (`static/css/style.css`) to create a modern, dynamic, and premium interface.

### Color Palette (CSS Variables)
Any newly added UI components must strictly utilize the existing CSS variable palette defined in `style.css`:
*   `--primary-color: #008080;` (Teal - used for primary buttons, active links, and brand emphasis)
*   `--secondary-color: #4db8b8;` (Light Teal/Cyan - used for gradients and hover states)
*   `--accent-color: #00e6e6;` (Bright Cyan - used for highlights)
*   `--bg-color: #f4f9f9;` (Very Light Teal/Gray - used for the main page background)
*   `--card-bg: #ffffff;` (Pure White - used for data cards and forms)
*   `--text-color: #1a3333;` (Dark Teal/Gray - used for primary text reading)
*   `--text-muted: #739999;` (Muted Teal - used for secondary text and labels)

### Design Elements & Micro-Interactions
*   **Gradients:** Primary buttons should maintain the dynamic gradient background: `linear-gradient(45deg, var(--primary-color), var(--secondary-color))`.
*   **Hover Effects:** Interactive cards and buttons must scale slightly (`transform: translateY(-5px)` or `scale(1.05)`) and increase drop-shadow opacity to provide tactile feedback to the user.
*   **Typography:** The application strictly uses the **Inter** font family from Google Fonts. Do not introduce secondary fonts without strong justification.
*   **Glassmorphism:** The navigation bar and authentication cards use subtle transparency and background-blur (`backdrop-filter: blur(10px)`). Preserve this aesthetic for any overlapping modal or top-level UI element.

### Responsiveness (Bootstrap Grid)
*   **Mobile-First Approach:** The UI must look excellent on mobile devices. Ensure padding and margins adjust dynamically (using Bootstrap's responsive spacing utilities like `p-3 p-md-5`).
*   **Grids:** When rendering lists of items (like Cylinders), always use responsive grid columns: `col-12 col-md-6 col-lg-4` to ensure a single column on mobile, two on tablets, and three on desktops.
*   **Navigation:** The navbar must collapse into a hamburger menu on screens smaller than the `lg` breakpoint.

---

### Agent Instructions summary:
Whenever generating new code or modifying existing code for this project:
1. Verify no security loopholes are introduced (especially missing CSRF tokens or unauthorized view access).
2. Follow the MVT structure strictly and do not deviate from the core app logic unless scaling up.
3. Use Bootstrap 5 classes combined with the defined CSS variables in `style.css`. Do not introduce hardcoded, inline HEX colors or random structural CSS. Maintain the modern, glassmorphic, and dynamic interactive feel.
