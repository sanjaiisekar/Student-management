# Student Management System (SMS)

A complete CRUD-based full-stack web application built following the
**Standard Operating Procedure (SOP) — Complete CRUD-Based Web Application Development**.

## 1. Project Overview
The Student Management System allows an institution to manage student records
through a web interface backed by a REST API and a relational database.
It implements full **Create, Read, Update, Delete (CRUD)** functionality with
client-side and server-side validation, automated tests, and API documentation.

## 2. Problem Statement
Educational institutions need a simple, reliable way to add, view, update,
search, and remove student records instead of relying on spreadsheets or
paper records, which are error-prone and hard to search or maintain.

## 3. Objectives
- Provide a responsive web interface for managing student records.
- Implement a RESTful backend API with full CRUD operations.
- Enforce data integrity through client-side and server-side validation.
- Persist data in a relational database (SQLite by default).
- Provide automated tests covering all CRUD scenarios.
- Document the API, architecture, and setup process.

## 4. Technology Stack
| Layer              | Technology                          |
|---------------------|--------------------------------------|
| Frontend            | HTML5, CSS3, Vanilla JavaScript (fetch API) |
| Backend             | Django 5 / Django REST Framework    |
| Database            | SQLite (default) — swappable for MySQL/PostgreSQL |
| API Testing         | Postman (collection included)       |
| Version Control     | Git / GitHub                        |

## 5. System Architecture
```
User → HTML/CSS/JavaScript Frontend → REST API →
Django REST Framework Backend → Django ORM → SQLite/MySQL/PostgreSQL Database
```
See `docs/ER_DIAGRAM.md` for the database design.

## 6. Project Folder Structure
```
student-management-system/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── config/            # Django project settings, URLs
│   └── students/          # Django app: models, serializers, views, tests
├── frontend/
│   ├── index.html
│   ├── css/style.css
│   └── js/app.js
├── docs/
│   ├── API_DOCUMENTATION.md
│   ├── ER_DIAGRAM.md
│   └── TESTING.md
├── .gitignore
└── README.md
```

## 7. Prerequisites
- Python 3.10+
- pip
- (Optional) virtualenv
- A modern web browser
- Postman (for API testing)

## 8. Installation & Execution Steps

### 8.1 Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # Configure environment variables
python manage.py migrate
python manage.py createsuperuser  # optional, for /admin access
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/api/students/`

### 8.2 Frontend Setup
The frontend is a static site — no build step required.
```bash
cd frontend
python -m http.server 5500
```
Open `http://127.0.0.1:5500` in your browser.

> The frontend calls the API at `http://127.0.0.1:8000/api`. Update the
> `API_BASE_URL` constant in `frontend/js/app.js` if your backend runs elsewhere.

### 8.3 Running Tests
```bash
cd backend
python manage.py test
```
See `docs/TESTING.md` for the full test plan and manual Postman test cases.

## 9. CRUD Functional Requirements
| Function | Student Activity                              |
|----------|------------------------------------------------|
| Create   | Fill the form with valid data and submit        |
| Read     | View the student list, search/filter by name/department |
| Update   | Click Edit on a record, modify fields, save      |
| Delete   | Click Delete on a record and confirm             |

## 10. Validation Rules
- `name`, `email`, `roll_number`, `department`, `year` are required.
- `email` must be a valid email format (validated client-side and server-side).
- `roll_number` must be unique.
- `year` must be an integer between 1 and 5.
- `phone` (optional) must be 10 digits if provided.
- Server-side validation always runs, even though client-side validation exists.

## 11. Security & Quality Guidelines Followed
- No hard-coded secrets — `SECRET_KEY` and `DEBUG` are read from environment
  variables via `.env` (see `.env.example`).
- Server-side validation implemented via DRF serializers.
- Django ORM used exclusively (no raw SQL) to prevent SQL injection.
- Frontend, backend, and database responsibilities are kept separate.
- CORS is explicitly configured for local frontend–backend communication.

## 12. Version Control
- `.gitignore` excludes virtual environments, `.env`, `__pycache__`, and the
  SQLite database file.
- Commit regularly with meaningful messages (see suggested commit strategy
  below).

### Suggested commit strategy
```
git init
git add .
git commit -m "chore: initial project structure"
git commit -m "feat: add Student model and migrations"
git commit -m "feat: add REST API CRUD endpoints"
git commit -m "feat: add frontend UI and API integration"
git commit -m "test: add backend CRUD test suite"
git commit -m "docs: add API documentation and ER diagram"
```

## 13. Future Enhancements
- Add authentication (JWT) for protected admin actions.
- Pagination and sorting on the student list endpoint.
- Bulk import/export (CSV).
- Migrate frontend to React per the SOP's alternative stack option.

## 14. Completion Checklist (per SOP Section 17)
- [x] Application starts without errors
- [x] Database connection works correctly
- [x] Create operation works
- [x] Read/list operation works
- [x] Update operation works
- [x] Delete operation works
- [x] Validation works (client + server)
- [x] Search/filter implemented
- [x] API endpoints documented and demonstrable
- [x] Source code and documentation included
