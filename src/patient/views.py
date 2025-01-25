from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Patient, FamilyMember, Medication
from .serializers import PatientSerializer, FamilyMemberSerializer, MedicationSerializer


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