from django.urls import path
from .views import PatientListCreateAPIView, PatientRetrieveAPIView, FamilyMemberListCreateAPIView, FamilyMemberRetrieveUpdateAPIView, UpdatePatient360APIView
from .views import MedicationListCreateAPIView, MedicationRetrieveUpdateAPIView, MedicationToggleActiveAPIView
from .views import Patient360APIView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

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

    path('patients/<int:pk>/360/', Patient360APIView.as_view(), name='patient-360'),
    path('patients/<int:patient_id>/360/update/', UpdatePatient360APIView.as_view(), name='update-patient-360'),

    # Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(template_name="swagger-ui.html", url_name="patient:schema"),name="swagger-ui"),
]