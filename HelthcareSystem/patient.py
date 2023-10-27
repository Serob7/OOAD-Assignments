from validators import not_empty_string, positive_integer_checker
from operations import Operatoins
from appointment import InPerson, Virtual
class Patient(Operatoins):
    @not_empty_string('Name', 1)
    @positive_integer_checker('Age', 2)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.medical_history = []

    def schedule_appt(self, doctor, appt_time):
        print(F'{self.name} requested to meet with {doctor.name} at {appt_time}')
        appt = InPerson(self, doctor, appt_time)
        doctor.requests[appt_time] = appt