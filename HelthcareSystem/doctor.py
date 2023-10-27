from validators import not_empty_string, email_checker
from operations import Operatoins

class Doctor:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    @not_empty_string('Speciality', 3)
    def __init__(self, name, contact_information, speciality):
        self.name = name
        self.contact_information = contact_information
        self.requests = {}
        self.appointments = {}

    def manage_appt(self):
        for request in self.requests:
            if request not in self.appointments:
                self.appointments[request] = self.requests[request]
                self.appointments[request].patient.medical_history.append(f'Appointment with {self.name}')
                print(f"Doctor {self.name} accepted appointment with {self.appointments[request].patient.name} at {request}")
            else:
                print(f"{request} is already booked")

    def view_history(self, patient):
        print(f"\t{patient.name}'s medical history")
        for history in patient.medical_history:
            print(history)
