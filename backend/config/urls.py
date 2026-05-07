from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.appointments.views import AppointmentViewSet
from apps.patients.views import PatientViewSet


router = DefaultRouter()
router.register(r"patients", PatientViewSet, basename="patient")
router.register(r"appointments", AppointmentViewSet, basename="appointment")


def health(_: object) -> JsonResponse:
    return JsonResponse({"status": "ok", "service": "jano-backend"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health, name="health"),
    path("api/", include(router.urls)),
]
