# 💼 Mini Invoice API for Freelancers

[![Django](https://img.shields.io/badge/Django-REST%20Framework-green)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Project%20Type-Mock%20Case%20Study-orange)](https://github.com/)
[![Time](https://img.shields.io/badge/Build%20Time-2%20Hours-success)]()

> A lightweight backend API designed to help freelancers generate and manage invoices quickly and efficiently using Django REST Framework.

---

## 🧩 Project Overview

This mock project demonstrates how a **simple backend system** can make life easier for freelancers who struggle with manual invoicing.  
It was completed in **under two hours** as part of a practical freelancing case study to showcase backend problem-solving skills.

---

## 🚨 Problem Statement

Freelancers and small business owners often rely on manual spreadsheets or Word templates to issue invoices — leading to:
- Time wasted on repetitive data entry  
- Missed or inconsistent payments  
- Difficulty tracking client payments  

This project offers a simple backend solution for those challenges.

---

## 🎯 Goal

To build a **minimal, functional API** that enables freelancers to:
- Create and manage invoices  
- Retrieve invoice lists and details  
- Update payment status  
- Delete invoices when necessary  

---

## 🧠 Approach

1. **Framework Choice:** Django REST Framework for rapid API development  
2. **Database:** SQLite (for simplicity and quick testing)  
3. **Core Features:**
   - CRUD operations for invoices  
   - Automatic timestamp creation  
   - Payment status tracking  

---

## ⚙️ Tech Stack

| Component | Tool/Framework |
|------------|----------------|
| **Language** | Python |
| **Backend Framework** | Django REST Framework |
| **Database** | SQLite |
| **Testing Tool** | Postman / Django Test Client |
| **Version Control** | Git & GitHub |

---

## 🧪 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/invoices/` | Create a new invoice |
| `GET` | `/invoices/` | Retrieve all invoices |
| `GET` | `/invoices/<id>/` | Retrieve a specific invoice |
| `PUT` | `/invoices/<id>/` | Update invoice (e.g., mark as paid) |
| `DELETE` | `/invoices/<id>/` | Delete an invoice |

---

## 🚀 Demo (Local Setup)

### 🧰 Prerequisites
Ensure you have the following installed:
- Python 3.10+
- pip
- virtualenv

### 🛠️ Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/mini-invoice-api.git
cd mini-invoice-api

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run migrations
python manage.py migrate

# 5️⃣ Start the server
python manage.py runserver

Visit your API at:
👉 http://127.0.0.1:8000/api/invoices/

🧾 Example JSON Payload
Create Invoice
POST /invoices/
{
  "client_name": "Jane Doe",
  "description": "Content Writing Project",
  "amount": 150.00,
  "status": "Pending"
}

Response
{
  "id": 1,
  "client_name": "Jane Doe",
  "description": "Content Writing Project",
  "amount": 150.00,
  "status": "Pending",
  "created_at": "2025-11-11T10:00:00Z"
}

📊 Project Impact

Reduces manual entry time for freelancers

Improves billing accuracy and client transparency

Can evolve into a full-scale SaaS invoicing system

🌱 Future Enhancements

🔐 Add user authentication

💳 Integrate payment gateway (e.g., PayPal/Stripe)

☁️ Deploy on Render or Railway for public API access

🧭 Case Study Summary
Aspect	Description
Project Type	Mock Case Study (Backend)
Duration	2 Hours
Main Skills	RESTful API Design, Data Modeling, Django, CRUD
Audience	Freelancers / Small Business Owners

💡 Reflection

“Even a small, focused backend project can make a big impact. By automating invoicing tasks, freelancers can save time and reduce errors — proving that simplicity and functionality go hand in hand.”

🌍 Connect With Me

👩‍💻 Blessing Ebele Anochili
🎯 Backend Developer | Translator | Software Engineer
📍 Lagos, Nigeria
🔗 https://www.linkedin.com/in/blessing-ebele-anochili/
 • https://www.github.com/in/blessing-ebele-anochili/

⭐ If you found this useful, don’t forget to give this repo a star!