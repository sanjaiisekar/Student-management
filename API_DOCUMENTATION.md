# API Documentation

Base URL: `http://127.0.0.1:8000/api/`

## Student Endpoints

| Operation | HTTP Method | Endpoint                 | Description                     |
|-----------|-------------|---------------------------|----------------------------------|
| Create    | POST        | `/api/students/`          | Create a new student record     |
| Read All  | GET         | `/api/students/`          | List all students (paginated)   |
| Read All (search) | GET | `/api/students/?search=<query>` | Search by name, roll number, department, or email |
| Read One  | GET         | `/api/students/{id}/`     | Retrieve one student by ID      |
| Update    | PUT/PATCH   | `/api/students/{id}/`     | Update a student record         |
| Delete    | DELETE      | `/api/students/{id}/`     | Delete a student record         |

## Request / Response Examples

### Create — `POST /api/students/`
Request body:
```json
{
  "name": "Asha Rao",
  "email": "asha.rao@example.com",
  "roll_number": "CS101",
  "department": "Computer Science",
  "year": 2,
  "phone": "9876543210"
}
```
Success response — `201 Created`:
```json
{
  "id": 1,
  "name": "Asha Rao",
  "email": "asha.rao@example.com",
  "roll_number": "CS101",
  "department": "Computer Science",
  "year": 2,
  "phone": "9876543210",
  "created_at": "2026-09-16T08:00:00Z",
  "updated_at": "2026-09-16T08:00:00Z"
}
```
Validation error response — `400 Bad Request`:
```json
{
  "email": ["Enter a valid email address."]
}
```

### Read All — `GET /api/students/`
Success response — `200 OK`:
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [ { "id": 1, "name": "Asha Rao", "...": "..." } ]
}
```

### Update — `PUT /api/students/1/`
Request body: same shape as Create.
Success response — `200 OK` with the updated record.

### Delete — `DELETE /api/students/1/`
Success response — `200 OK`:
```json
{ "message": "Student deleted successfully." }
```
Not found — `404 Not Found` if the ID does not exist.

## Field Validation Rules
| Field         | Rule                                              |
|---------------|-----------------------------------------------------|
| name          | Required, non-empty                                |
| email         | Required, valid email format, unique                |
| roll_number   | Required, non-empty, unique                          |
| department    | Required, non-empty                                  |
| year          | Required, integer 1–5                                |
| phone         | Optional, exactly 10 digits if provided              |

## Postman
Import the endpoints above into Postman, or generate a collection from
`http://127.0.0.1:8000/api/students/` while the server is running.
Set the `Content-Type: application/json` header on POST/PUT requests.
