from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from apps.patients.models import Patient


class ApiSmokeTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.username = "doctor"
        self.password = "StrongPass123!"
        user_model = get_user_model()
        user_model.objects.create_user(username=self.username, password=self.password)

        token_response = self.client.post(
            "/api/token/",
            {"username": self.username, "password": self.password},
            format="json",
        )
        access = token_response.json()["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

    def test_health_endpoint(self) -> None:
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_patients_require_auth(self) -> None:
        anon = APIClient()
        response = anon.get("/api/patients/")
        self.assertEqual(response.status_code, 401)

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

    def test_reject_past_appointment(self) -> None:
        patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1990-01-01",
            phone="+251911111111",
        )
        payload = {
            "patient": patient.id,
            "scheduled_for": (timezone.now() - timedelta(hours=2)).isoformat(),
            "reason": "Follow-up",
            "status": "scheduled",
        }
        response = self.client.post("/api/appointments/", payload, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("scheduled_for", response.json())

    def test_filter_appointments_by_patient(self) -> None:
        patient_1 = Patient.objects.create(first_name="A", last_name="One", date_of_birth="1990-01-01")
        patient_2 = Patient.objects.create(first_name="B", last_name="Two", date_of_birth="1991-01-01")

        future_1 = timezone.now() + timedelta(days=1)
        future_2 = timezone.now() + timedelta(days=2)

        self.client.post(
            "/api/appointments/",
            {
                "patient": patient_1.id,
                "scheduled_for": future_1.isoformat(),
                "reason": "Consultation",
                "status": "scheduled",
            },
            format="json",
        )
        self.client.post(
            "/api/appointments/",
            {
                "patient": patient_2.id,
                "scheduled_for": future_2.isoformat(),
                "reason": "Checkup",
                "status": "scheduled",
            },
            format="json",
        )

        response = self.client.get(f"/api/appointments/?patient={patient_1.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 1)
        self.assertEqual(len(response.json()["results"]), 1)
        self.assertEqual(response.json()["results"][0]["patient"], patient_1.id)

    def test_reject_duplicate_appointment_slot_for_same_patient(self) -> None:
        patient = Patient.objects.create(first_name="Dup", last_name="Case", date_of_birth="1991-08-12")
        slot = timezone.now() + timedelta(days=1, hours=3)

        first = self.client.post(
            "/api/appointments/",
            {
                "patient": patient.id,
                "scheduled_for": slot.isoformat(),
                "reason": "Initial",
                "status": "scheduled",
            },
            format="json",
        )
        self.assertEqual(first.status_code, 201)

        duplicate = self.client.post(
            "/api/appointments/",
            {
                "patient": patient.id,
                "scheduled_for": slot.isoformat(),
                "reason": "Duplicate",
                "status": "scheduled",
            },
            format="json",
        )
        self.assertEqual(duplicate.status_code, 400)
        self.assertIn("scheduled_for", duplicate.json())
