### Patient Management System APIS

---

#### **Overview**

This project is a **Patient Management System** developed using **Django** and **Django REST Framework (DRF)**. It serves as an assessment to evaluate the proficiency in designing Django models, creating REST APIs, and implementing backend logic. The project is built to manage patient records, family member details, and prescribed medications efficiently.

---

### **Features**

1. **Patient Management**
   - Add, view, update, and retrieve patient details.
   - Key fields include:
     - Name
     - Date of Birth
     - Gender

2. **Family Member Management**
   - Associate family members with patients and define relationships.
   - Update family member details such as the relationship or emergency contact status.

3. **Medication Management**
   - Add, view, and manage active medications for patients.
   - Update dosage, timing, or activate/deactivate medications.

4. **Patient 360**
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
   cd patient-management-system
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate   # For Windows: env\Scripts\activate
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
   - Visit `http://127.0.0.1:8000/` for API endpoints.

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

#### **Patient 360**
- `GET /patients/<patient_id>/360/` - Retrieve patient demographics and family details.
- `PUT /patients/<patient_id>/360/update/` - Update patient demographics or family details.

---

### **Bonus Features**
1. **Code Quality**
   - Follows **SOLID principles** for better maintainability.
   - Modularized structure for scalability.
   
2. **Filtering in APIs**
   - Add filters to APIs (e.g., filter patients by gender, medications by active status).

3. **Database Optimization**
   - Efficient query handling using `select_related` and `prefetch_related`.

4. **Nested Serializers**
   - Proper use of nested serializers for related objects.

---

### **Assumptions**
- Emergency contacts are managed as part of the family members.
- Basic validations are applied to all models and serializers.
- SQLite is used as the default database but can be switched to PostgreSQL.

---

### **Future Enhancements**
- Add authentication and authorization to secure the APIs.
- Implement soft deletes for patients and related records.
- Introduce pagination in list APIs.
- Create a frontend for ease of use.

---

### **Feedback**
If you have any feedback or suggestions, please reach out via the repository issue tracker or email us at [support@example.com](mailto:support@example.com).

---

Enjoy exploring the **Patient Management System**!