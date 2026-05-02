# Admin Portal - Inventory & Reports UI Issues
Project: BookMyGas (Sri Lanka Gas Booking System)

---

## 1. Inventory Table Action Buttons (Edit/Delete)

### URL
http://localhost:8001/inventory/

### Problem
- "Edit" and "Delete" buttons currently use text
- UI looks cluttered and inconsistent

### Expected Behavior
- Replace text buttons with **icon-only buttons**

### UI Requirements
- Use icons:
  - Edit → Pencil icon
  - Delete → Trash icon
- Add tooltip on hover:
  - "Edit"
  - "Delete"
- Maintain clickable area (min 36x36px)

### Design Notes
- Keep minimal style (no heavy background)
- Use subtle hover effect

### Acceptance Criteria
- No text shown in action buttons
- Icons clearly visible and accessible
- Hover tooltip works correctly

---

## 2. Inventory Table Column Width (Type Column)

### Problem
- "Type" column is too narrow
- Content wraps or looks cramped

### Expected Behavior
- Increase width of "Type" column

### UI Requirements
- Apply:
  - `min-width: 180px` (or suitable value)
- Prevent text breaking:
  - `white-space: nowrap`

### Acceptance Criteria
- Column content fully visible
- Table layout remains balanced

---

## 3. Filter Dropdown UI Consistency

### Problem
- "Filter by Status" and "Filter by Method" dropdowns are inconsistent
- Styling differs from rest of the project

### Expected Behavior
- Use **single reusable dropdown component**

### UI Requirements
- Same:
  - Height
  - Padding
  - Border radius
  - Font size
- Add consistent:
  - Focus state
  - Hover state

### Design Notes
- Match overall project theme
- Avoid default browser styles

### Acceptance Criteria
- All dropdowns look identical
- Smooth interaction and focus states

---

## 4. Date & Time Picker UI Standardization

### Problem
- Date/time picker does not match project UI
- Feels disconnected from design system

### Expected Behavior
- Use a **custom styled date & time picker**

### UI Requirements
- Separate UI for:
  - Date picker
  - Time picker
- Consistent with:
  - Input fields
  - Dropdown styles

### Suggested Approach
- Use libraries (if needed):
  - React DatePicker / Flatpickr
- Apply custom theme

### Acceptance Criteria
- Matches project UI
- Easy to use on desktop & mobile
- No default browser styling

---

## 5. Reports Export Functionality

### Problem
- Reports cannot be exported

### Expected Behavior
- Allow exporting reports in multiple formats

### Required Export Formats
- PDF
- Excel (XLSX) *(recommended instead of XML for usability)*

### Functional Requirements
- Export button in Reports page
- Allow user to:
  - Export current filtered data
  - Export full dataset

### UI Requirements
- Buttons:
  - "Export as PDF"
  - "Export as Excel"

### Acceptance Criteria
- File downloads successfully
- Data matches UI table
- Proper formatting in exported file

---

## 6. Reports UI Improvements

### Problem
- Reports section lacks usability features

### Expected Behavior
- Add filters and structured layout

### Required Features
- Filter by:
  - Date range
  - Payment method
  - Booking type (Delivery / Pickup)

### UI Components
- Filter bar (top section)
- Table + summary cards

### Acceptance Criteria
- Filters update data correctly
- UI remains clean and responsive

---

## Notes
- Focus on **reusable UI components**
- Maintain **design consistency across admin portal**
- Prefer **minimal + professional UI**
