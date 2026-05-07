from django.utils import timezone
from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["id", "patient", "scheduled_for", "reason", "status", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_scheduled_for(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Appointment must be scheduled in the future.")
        return value
