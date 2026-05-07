from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related("patient").order_by("scheduled_for")
    serializer_class = AppointmentSerializer
