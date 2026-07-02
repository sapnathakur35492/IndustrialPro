# IndustrialPro

Django-based industrial company website with product catalog, company information, and contact/RFQ features.

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Apps

- **core** — Home, about, contact, gallery
- **catalog** — Products and industries
- **company** — Capabilities, infrastructure, certifications
