from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Patient, FamilyMember, Medication
from .serializers import PatientSerializer, FamilyMemberSerializer, MedicationSerializer, Patient360Serializer


class PatientListCreateAPIView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class FamilyMemberListCreateAPIView(ListCreateAPIView):
    serializer_class = FamilyMemberSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return FamilyMember.objects.filter(patient__id=patient_id)

    def perform_create(self, serializer):
        patient_id = self.kwargs['patient_id']
        patient = Patient.objects.get(id=patient_id)
        serializer.save(patient=patient)

class FamilyMemberRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = FamilyMemberSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return FamilyMember.objects.filter(patient__id=patient_id)


# i. Add an Active Medication & ii. List All Active Medications
class MedicationListCreateAPIView(ListCreateAPIView):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Medication.objects.filter(patient_id=patient_id, is_active=True)

    def perform_create(self, serializer):
        patient_id = self.kwargs.get('patient_id')
        try:
            patient = Patient.objects.get(id=patient_id)
            serializer.save(patient=patient, is_active=True)
        except Patient.DoesNotExist:
            raise serializer.ValidationError({"error": "Patient not found."})


# iii. Retrieve a Given Medication & v. Update Medication Details
class MedicationRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Medication.objects.filter(patient_id=patient_id)


# iv. Activate or Deactivate Medications
class MedicationToggleActiveAPIView(APIView):
    def post(self, request, patient_id, pk):
        try:
            medication = Medication.objects.get(patient_id=patient_id, id=pk)
            medication.is_active = not medication.is_active
            medication.save()
            return Response(
                {"message": f"Medication status changed to {'Active' if medication.is_active else 'Inactive'}."},
                status=status.HTTP_200_OK,
            )
        except Medication.DoesNotExist:
            return Response({"error": "Medication not found."}, status=status.HTTP_404_NOT_FOUND)
    

class Patient360APIView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = Patient360Serializer

    def retrieve(self, request, *args, **kwargs):
        try:
            patient = self.get_object()
            serializer = self.get_serializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)


class UpdatePatient360APIView(APIView):
    def put(self, request, patient_id):
        try:
            # Retrieve the patient
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data

        # Update patient demographics if provided
        if 'patient' in data:
            patient_serializer = Patient360Serializer(patient, data=data['patient'], partial=True)
            if patient_serializer.is_valid():
                patient_serializer.save()
            else:
                return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update family members if provided
        if 'family_members' in data:
            for family_member_data in data['family_members']:
                family_member_id = family_member_data.pop('id', None)
                if family_member_id:
                    try:
                        family_member = FamilyMember.objects.get(id=family_member_id, patient=patient)
                        family_member_serializer = FamilyMemberSerializer(
                            family_member, data=family_member_data, partial=True
                        )
                        if family_member_serializer.is_valid():
                            family_member_serializer.save()
                        else:
                            return Response(family_member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    except FamilyMember.DoesNotExist:
                        return Response(
                            {"error": f"Family member with ID {family_member_id} not found."},
                            status=status.HTTP_404_NOT_FOUND,
                        )
                else:
                    return Response({"error": "Family member ID is required for updates."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Patient 360 updated successfully."}, status=status.HTTP_200_OK)