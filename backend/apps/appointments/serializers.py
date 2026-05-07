from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["id", "patient", "scheduled_for", "reason", "status", "created_at"]
        read_only_fields = ["id", "created_at"]
