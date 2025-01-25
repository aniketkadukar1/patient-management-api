from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FamilyMember(models.Model):
    RELATIONSHIP_CHOICES = [
        ('Parent', 'Parent'),
        ('Sibling', 'Sibling'),
        ('Child', 'Child'),
        ('Spouse', 'Spouse'),
        ('Other', 'Other'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='family_members')
    related_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='related_family_members')
    relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)

    def __str__(self):
        return f"{self.patient.name} is {self.relationship} of {self.related_patient.name}"



class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medications')
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)  # e.g., "500 mg"
    frequency = models.CharField(max_length=100)  # e.g., "Twice a day"
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Optional for ongoing medications
    instructions = models.TextField(blank=True, null=True)  # Additional instructions for usage
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.medication_name} for {self.patient.name}"

