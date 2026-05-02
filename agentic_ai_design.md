# Agentic AI Design (Updated)
## BookMyGas – Gas Cylinder Find & Booking System

---

## 1. Overview

This document defines how Agentic AI can be integrated into the existing BookMyGas system without disrupting current functionality.

The system already includes:
- Public booking portal (gas_booking)
- Admin management portal (gas_admin)
- Shared core app (models, logic)

AI will act as an enhancement layer, not a replacement.

---

## 2. Current System Alignment

### Existing Features
- Cylinder filtering (location, type, supplier)
- Booking system with status tracking
- Admin inventory & booking control
- Secure authentication & RBAC

### AI Value Add
- Intelligent ranking
- Personalization
- Demand insights
- Smart assistant

---

## 3. AI Integration Strategy

User → Django → AI Layer → Django Validation → UI

---

## 4. Use Cases

### Smart Recommendation
- Rank cylinders by price, location, availability

### Booking Assistant
- Convert chat to structured booking actions

### Admin Insights
- Predict demand and stock needs

### Fraud Detection
- Flag suspicious booking patterns

---

## 5. Integration Example

In core/views.py:

Before:
cylinders = Cylinder.objects.filter(...)

After:
cylinders = Cylinder.objects.filter(...)
cylinders = ai_rank_cylinders(user, cylinders)

---

## 6. AI Service Layer

File: core/ai_service.py

Example:
def ai_rank_cylinders(user, cylinders):
    pass

---

## 7. Prompt Example

You are an assistant for BookMyGas.

Rank gas cylinders based on:
- Location
- Price
- Availability

Return JSON with id, reason, score.

---

## 8. Safety Rules

AI MUST NOT:
- Approve bookings
- Modify database

Django validates everything.

---

## 9. Conclusion

AI enhances UX and decision-making but does not replace core logic.
