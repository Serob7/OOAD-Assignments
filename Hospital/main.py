from patient import Patient
from medical_procedures import Surgery, CheckUp, CheckIn, CheckOut
from doctor import Doctor
from medical_staff import MedicalStaff

def main():
    #creating Patient instance
    patient = Patient('Serob', 25)

    #create Doctor instance, make appointment
    doctor = Doctor('Armen', 'armen@gmail.com')
    doctor.make_appointment('28.10.2023', patient)

    #medical staff managing operations
    med = MedicalStaff('Tom', 'receptionist')
    med.check_in(patient)

    #crating procedure instances
    checkup = CheckUp('Annual check-up')
    surgery = Surgery('Plastic surgery')
    checkup.perform(doctor, patient)
    surgery.perform(doctor, patient)

    med.check_out(patient)

    #view patient's history

    print(f"\nPatient {patient.name}'s medical history" )
    doctor.view_patients_medical_history(patient)

if __name__ == '__main__':
    main()