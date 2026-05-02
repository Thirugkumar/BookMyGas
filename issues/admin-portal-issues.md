# Admin Portal - Issues & Feature Requirements
Project: BookMyGas (Sri Lanka Gas Booking System)

---

## 1. Booking Update Modal UI Issue

### URL
http://localhost:8001/bookings/

### Problem
- When clicking "Update" on a booking, the modal content is partially hidden
- Users cannot clearly see or interact with all fields

### Possible Causes
- Overflow issues
- Fixed height modal
- Missing scroll behavior
- Z-index or positioning problems

### Expected Behavior
- Modal should be fully visible within viewport
- If content exceeds height → enable vertical scrolling

### UI Requirements
- Max height: `90vh`
- Enable:
  - `overflow-y: auto`
- Add proper padding
- Ensure modal is centered

### Acceptance Criteria
- All form fields are accessible
- No content cut-off
- Works on all screen sizes

---

## 2. Admin Sidebar Enhancement

### Problem
- Sidebar is incomplete
- Missing essential admin features

### Expected Behavior
Add structured sidebar navigation with separate pages:

### Required Sidebar Items

#### Core Modules
- Dashboard
- Bookings
- Customers
- Inventory
- Payments
- Reports

---

## 3. Separate Pages for Each Module

### Problem
- Sidebar items are not properly routed
- No dedicated pages per feature

### Expected Behavior
Each sidebar item must navigate to a **separate page/view**

### Required Routes Structure

- `/dashboard`
- `/bookings`
- `/customers`
- `/inventory`
- `/payments`
- `/reports`

### Acceptance Criteria
- Each route loads independently
- No overlapping UI
- Proper page titles and headers

---

## 4. Inventory Management Module

### Feature Requirement

### Purpose
Manage gas cylinder stock levels

### Functional Requirements
- Add new stock
- Update stock quantity
- View available cylinders
- Track low stock alerts

### UI Requirements
- Table view:
  - Cylinder Type
  - Quantity Available
  - Last Updated
- Actions:
  - Edit
  - Update Stock

### Acceptance Criteria
- Admin can manage stock easily
- Real-time updates reflected

---

## 5. Payments Management Module

### Feature Requirement

### Purpose
Track and manage payments

### Functional Requirements
- View all transactions
- Filter by:
  - Payment method (Card / COD)
  - Date
- Payment status:
  - Paid
  - Pending
  - Failed

### UI Requirements
- Table view:
  - Booking ID
  - Customer Name
  - Payment Method
  - Amount
  - Status

### Acceptance Criteria
- Accurate payment tracking
- Easy filtering and search

---

## 6. Reports Module

### Feature Requirement

### Purpose
Provide business insights

### Reports Needed
- Daily bookings
- Monthly revenue
- Delivery vs Pickup stats
- Payment method breakdown

### UI Requirements
- Simple charts (bar / line)
- Summary cards:
  - Total bookings
  - Total revenue

### Acceptance Criteria
- Data is accurate
- Easy to understand visuals

---

## 7. Sidebar UX Improvements

### Problem
Sidebar lacks structure and usability

### Expected Behavior
- Highlight active menu item
- Collapsible sidebar (optional)
- Icons optional (keep minimal)

### UI Requirements
- Clear spacing
- Hover effect
- Active state indicator

### Acceptance Criteria
- Easy navigation
- Clean and modern layout

---

## 8. General Admin UI Improvements

### Requirements
- Consistent spacing and layout
- Reusable components:
  - Tables
  - Forms
  - Modals
- Responsive design

### Acceptance Criteria
- UI consistency across all pages
- No broken layouts

---

## Notes
- Follow **modular architecture**
- Keep UI **minimal and functional**
- Prioritize **usability over decoration**
