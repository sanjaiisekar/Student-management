"""
Test suite covering CRUD operations with valid, missing, duplicate,
and invalid data — per SOP Section 10: Testing Procedure.
"""
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Student


class StudentCRUDTests(APITestCase):

    def setUp(self):
        self.list_url = '/api/students/'
        self.valid_payload = {
            'name': 'Asha Rao',
            'email': 'asha.rao@example.com',
            'roll_number': 'CS101',
            'department': 'Computer Science',
            'year': 2,
            'phone': '9876543210',
        }
        self.student = Student.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            roll_number='CS100',
            department='Computer Science',
            year=1,
        )

    # ---------- CREATE ----------
    def test_create_with_valid_data(self):
        response = self.client.post(self.list_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    def test_create_with_missing_required_field(self):
        payload = self.valid_payload.copy()
        del payload['name']
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_create_with_duplicate_roll_number(self):
        payload = self.valid_payload.copy()
        payload['roll_number'] = 'CS100'  # already used in setUp
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_invalid_email(self):
        payload = self.valid_payload.copy()
        payload['email'] = 'not-an-email'
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_invalid_year(self):
        payload = self.valid_payload.copy()
        payload['year'] = 9
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ---------- READ ----------
    def test_read_list_populated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_read_list_empty(self):
        Student.objects.all().delete()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

    def test_read_single_valid_id(self):
        response = self.client.get(f'{self.list_url}{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['roll_number'], 'CS100')

    def test_read_single_invalid_id(self):
        response = self.client.get(f'{self.list_url}99999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ---------- UPDATE ----------
    def test_update_with_valid_id(self):
        response = self.client.patch(
            f'{self.list_url}{self.student.id}/', {'department': 'IT'}, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.department, 'IT')

    def test_update_with_invalid_id(self):
        response = self.client.patch(
            f'{self.list_url}99999/', {'department': 'IT'}, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ---------- DELETE ----------
    def test_delete_with_valid_id(self):
        response = self.client.delete(f'{self.list_url}{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())

    def test_delete_with_invalid_id(self):
        response = self.client.delete(f'{self.list_url}99999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ---------- SEARCH ----------
    def test_search_by_name(self):
        response = self.client.get(self.list_url, {'search': 'John'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
