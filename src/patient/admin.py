from django.contrib import admin
from .models import Medication, Patient, FamilyMember

# Register your models here.
admin.site.register(Medication)
admin.site.register(Patient)
admin.site.register(FamilyMember)

