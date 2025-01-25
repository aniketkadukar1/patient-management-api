from django.urls import path
from .views import PatientListCreateAPIView, PatientRetrieveAPIView, FamilyMemberListCreateAPIView, FamilyMemberRetrieveUpdateAPIView
from .views import MedicationListCreateAPIView, MedicationRetrieveUpdateAPIView, MedicationToggleActiveAPIView

app_name = 'patient'

urlpatterns = [
    path('patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveAPIView.as_view(), name='patient-retrieve-update'),
        # Family member APIs
    path('patients/<int:patient_id>/family-members/', FamilyMemberListCreateAPIView.as_view(), name='family-member-list-create'),
    path('patients/<int:patient_id>/family-members/<int:pk>/', FamilyMemberRetrieveUpdateAPIView.as_view(), name='family-member-retrieve-update'),

    path('patients/<int:patient_id>/medications/', MedicationListCreateAPIView.as_view(), name='medication-list-create'),
    path('patients/<int:patient_id>/medications/<int:pk>/', MedicationRetrieveUpdateAPIView.as_view(), name='medication-retrieve-update'),
    path('patients/<int:patient_id>/medications/<int:pk>/toggle/', MedicationToggleActiveAPIView.as_view(), name='medication-toggle-active'),
]