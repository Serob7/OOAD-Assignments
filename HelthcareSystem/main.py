from patient import Patient
from doctor import Doctor
from appointment import  Appointment

def main():
    #create Patient and Doctor instances
    patient = Patient('Serob', 25)
    doctor = Doctor('Tom', 'tom@gmial.com', 'Therapist')

    #schedule appt
    patient.schedule_appt(doctor, '3:45')

    #manage schedules
    doctor.manage_appt()

    #view med history
    print('Patient views')
    patient.view_history()
    print('Doctor views')
    doctor.view_history(patient)


if __name__ == '__main__':
    main()