from rest_framework import serializers, routers
from .models import Medication, Patient, FamilyMember


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class FamilyMemberSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)  # Nested patient details
    # related_patient = PatientSerializer(read_only=True)  # Nested related patient details

    class Meta:
        model = FamilyMember
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    # patient = PatientSerializer(read_only=True)  # Nested patient details

    class Meta:
        model = Medication
        fields = '__all__'


