from django.test import TestCase
from rest_framework.test import APIClient


class ApiSmokeTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_health_endpoint(self) -> None:
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_create_patient(self) -> None:
        payload = {
            "first_name": "Jane",
            "last_name": "Doe",
            "date_of_birth": "1995-03-21",
            "phone": "+251900000000",
        }
        response = self.client.post("/api/patients/", payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["first_name"], "Jane")
