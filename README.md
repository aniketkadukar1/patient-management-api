### Patient Management APIS

---

#### **Overview**

This project is a **Patient Management API** developed using **Django** and **Django REST Framework (DRF)**.

---

### **Features**

1. **Patient Management**
   - Add, view, update, and retrieve patient details.
   - Key fields include:
     - Name
     - Date of Birth
     - Gender
     - Mobile number
     - Medical History

2. **Family Member Management**
   - Associate family members with patients and define relationships.
   - Update family member details such as the relationship or emergency contact status.

3. **Medication Management**
   - Add, view, and manage active medications for patients.
   - Update dosage, timing, or activate/deactivate medications.

4. **Patient Overall Information**
   - Retrieve complete details of a patient, including:
     - Demographics
     - Family members
   - Update patient demographics and family member details in a single API call.

---

### **Installation Guide**

Follow these steps to set up the project locally:

#### **Prerequisites**
- Python 3.8 or higher
- Django 4.0 or higher
- Django REST Framework (DRF)
- SQLite (default) or PostgreSQL for database (optional)

#### **Setup Instructions**
1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd patient-management-api
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the API**
   - Visit `http://127.0.0.1:8000/api/` for API endpoints.
   - Visit `http://localhost:8000/api/docs/` for swagger docs.

---

### **Endpoints**

#### **Patients**
- `POST /patients/` - Add a new patient.
- `GET /patients/` - List all patients.
- `GET /patients/<id>/` - Retrieve a patient's details.
- `PUT /patients/<id>/` - Update a patient's details.

#### **Family Members**
- `POST /patients/<patient_id>/family-members/` - Add a family member for a patient.
- `GET /patients/<patient_id>/family-members/` - List all family members of a patient.
- `GET /patients/<patient_id>/family-members/<id>/` - Retrieve a specific family member.
- `PUT /patients/<patient_id>/family-members/<id>/` - Update a family member's details.

#### **Medications**
- `POST /patients/<patient_id>/medications/` - Add a medication for a patient.
- `GET /patients/<patient_id>/medications/` - List all active medications for a patient.
- `GET /patients/<patient_id>/medications/<id>/` - Retrieve a specific medication.
- `PUT /patients/<patient_id>/medications/<id>/` - Update medication details (dosage, timings, etc.).
- `PATCH /patients/<patient_id>/medications/<id>/activate/` - Activate or deactivate a medication.

#### **Patient's Overall Data**
- `GET /patients/<patient_id>/360/` - Retrieve patient demographics and family details.
- `PUT /patients/<patient_id>/360/update/` - Update patient demographics or family details.

---

### **Future Enhancements**
- Add authentication and authorization to secure the APIs.
- Implement soft deletes for patients and related records.
- Introduce pagination in list APIs.
- Create a frontend for ease of use.

---
