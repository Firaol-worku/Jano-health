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

    def validate(self, attrs):
        patient = attrs.get("patient")
        scheduled_for = attrs.get("scheduled_for")

        existing = Appointment.objects.filter(patient=patient, scheduled_for=scheduled_for)
        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise serializers.ValidationError(
                {"scheduled_for": "Patient already has an appointment at this time."}
            )

        return attrs
