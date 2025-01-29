from rest_framework import serializers, routers
from .models import Medication, Patient, FamilyMember
from django.contrib.auth.models import User

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


class Patient360Serializer(serializers.ModelSerializer):
    family_members = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'name', 'dob', 'gender', 'family_members']

    def get_family_members(self, obj):
        family_members = FamilyMember.objects.filter(patient=obj)
        return FamilyMemberSerializer(family_members, many=True).data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user