# Public Portal - Issues & Fix Requirements
Project: BookMyGas (Sri Lanka Gas Booking System)

---

## 1. Booking Flow Not Working Properly

### Problem
Users are unable to complete the gas booking process smoothly.

### Current Flow Issues
- "Book Now" button opens booking section but lacks structured flow
- Multiple inputs appear without proper step-by-step guidance
- No clear validation or progression

### Expected Behavior
Implement a **multi-step booking flow (wizard)**:

#### Step 1: Select Date & Time
- User selects preferred delivery/pickup date and time

#### Step 2: Delivery Method
- Options:
  - Home Delivery
  - Store Pickup

#### Step 3: Conditional Inputs
- If Delivery:
  - Address field required
- If Pickup:
  - Skip address

#### Step 4: Payment Method
- Card Payment
- Cash on Delivery (COD)

#### Step 5: Personal Details
- Name
- Phone Number
- Address (if delivery)

#### Step 6: Confirmation
- Show summary before final confirmation

#### Step 7: Success Modal
- Show:
  - Booking Reference ID
  - Success Message
  - Friendly UX message (e.g., "Your gas is on the way!")

### Acceptance Criteria
- Booking must complete without errors
- Step-by-step UI (no clutter)
- Proper validation for all fields
- Success modal must display booking reference

---

## 2. Card UI Consistency Issue

### Problem
Cards have inconsistent heights and button alignment.

### Expected Behavior
- All cards should have:
  - Equal height
  - Consistent padding
  - Buttons aligned at the bottom

### UI Requirement
- Use Flexbox:
  - `display: flex`
  - `flex-direction: column`
  - `justify-content: space-between`

### Acceptance Criteria
- All cards visually aligned
- Buttons positioned consistently at bottom

---

## 3. Button Consistency Issue

### Problem
Buttons across the UI are inconsistent in size and alignment.

### Expected Behavior
- Uniform:
  - Height
  - Width (where applicable)
  - Border radius
  - Font size

### Acceptance Criteria
- All primary buttons look identical
- No layout shift between cards

---

## 4. Navbar UI Improvements

### Problem
- Icons are unnecessary
- Active state not clearly visible

### Expected Behavior
- Remove icons from nav items
- Add underline for:
  - Active nav item
  - Hover state

### UI Behavior
- Smooth underline animation on hover
- Minimal and clean style

### Acceptance Criteria
- Active page clearly highlighted
- Hover animation smooth and subtle

---

## 5. Footer UI Enhancement

### Problem
Footer looks plain and outdated

### Expected Behavior
- Apply **Glassmorphism effect**

### UI Requirements
- Semi-transparent background
- Blur effect
- Soft border
- Slight color tint

### Acceptance Criteria
- Modern glass-like appearance
- Matches overall theme

---

## 6. Navbar Glassmorphism Design

### Problem
Navbar lacks modern UI styling

### Expected Behavior
- Apply Glassmorphism:
  - Transparent background
  - Blur effect
  - Sticky top

### Acceptance Criteria
- Navbar looks modern and clean
- Works on scroll without breaking UI

---

## Notes
- Focus on **clean UX and minimal design**
- Ensure **mobile responsiveness**
- Avoid cluttered UI
