from validators import not_empty_string, email_checker

class Doctor:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.appointments = []

    def make_appointment(self, date, patient):
        appt = f'Patient {patient.name} at {date}'
        self.appointments.append(appt)
        return appt


    def view_patients_medical_history(self, patient):
        for history in patient.medical_history:
            print(history.name)
