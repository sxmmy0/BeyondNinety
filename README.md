# ⚽ BYD90 (Beyond Ninety)

**BYD90** is a full-stack football performance platform helping players train smarter, connect with coaches, and track progress beyond the 90 minutes of match time.

---

## 🚀 Features

- User registration and JWT login
- Protected dashboard
- React + TypeScript + Tailwind frontend
- Django + PostgreSQL backend with Django REST Framework
- CORS-secured communication between frontend and backend
- Coach and player profile models (in progress)
- Drill browsing and booking (coming soon)

---

## 🧱 Tech Stack

| Frontend             | Backend                | Other                 |
|----------------------|------------------------|------------------------|
| React + TypeScript   | Python + Django        | Docker (coming soon)  |
| TailwindCSS          | Django REST Framework  | JWT Auth (SimpleJWT)  |
| Axios (API calls)    | PostgreSQL             | Vercel / Render-ready |

---

## 🔧 Local Setup

### Prerequisites

- Python 3.10+
- Node.js + npm
- PostgreSQL (installed and running)

---

## 🐍 Backend Setup (Django)

```bash
# 1. Navigate to backend directory
cd backend

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```
## Navigate to frontend
```
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install --legacy-peer-deps

# 3. Start dev server
npm start
```
---
✅ To-Do / Coming Soon
Booking system (players ↔ coaches)

Drill filtering + video previews

Stripe or PayPal integration for session payments

Profile photo uploads

Mobile version (React Native)
---
📫 Contact
Made by Samuel Obembe

GitHub: @sxmmy

Instagram: @beyondninety

Email: sam@beyondninety.com (coming soon)
---
© 2025 Samuel Obembe. All rights reserved.  
BYD90 is a proprietary platform and may not be copied or reused without written permission.

