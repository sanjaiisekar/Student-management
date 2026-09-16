# Testing Documentation

## 1. Automated Tests (Backend)
Location: `backend/students/tests.py`
Run with:
```bash
cd backend
python manage.py test
```

### Test Coverage
| Area   | Scenarios Covered                                              |
|--------|-------------------------------------------------------------------|
| Create | Valid data, missing required field, duplicate roll number, invalid email, invalid year |
| Read   | List populated, list empty, retrieve valid ID, retrieve invalid ID |
| Update | Valid ID, invalid ID                                               |
| Delete | Valid ID, invalid ID                                               |
| Search | Filter by name                                                    |

## 2. Manual API Testing (Postman)
1. Start the backend: `python manage.py runserver`
2. Open Postman and set base URL to `http://127.0.0.1:8000/api/students/`
3. Test each endpoint independently:
   - **POST** with valid data → expect `201`
   - **POST** with missing fields → expect `400`
   - **POST** with duplicate roll number/email → expect `400`
   - **GET** list → expect `200` with results array
   - **GET** single valid ID → expect `200`
   - **GET** single invalid ID → expect `404`
   - **PUT/PATCH** valid ID → expect `200` with updated data
   - **PUT/PATCH** invalid ID → expect `404`
   - **DELETE** valid ID → expect `200`
   - **DELETE** invalid ID → expect `404`
4. After each write operation, verify the database state using
   `python manage.py shell` or the Django admin at `/admin/`.

## 3. Frontend Testing Checklist
- [ ] Form rejects empty required fields (client-side validation)
- [ ] Form rejects invalid email format
- [ ] Form rejects invalid phone format
- [ ] Server-side validation errors are displayed if they slip past the client
- [ ] Create adds a new row to the table without a full page reload
- [ ] Edit pre-fills the form and updates the correct record
- [ ] Delete asks for confirmation and removes the row
- [ ] Search box filters the list as you type
- [ ] Layout is usable on both desktop and mobile screen widths
- [ ] Clear error message is shown if the backend is unreachable

## 4. Error Handling Testing
- Stop the Django server and attempt to load the frontend — confirm a
  user-friendly error message is shown instead of a silent failure.
- Submit a form with the backend offline — confirm the UI does not crash.
