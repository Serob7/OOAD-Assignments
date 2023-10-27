from validators import not_empty_string
from abc import ABC, abstractmethod

class Appointment(ABC):
    @abstractmethod
    def __init__(self, patient, doctor, appt_time):
        ...

class InPerson(Appointment):
    @not_empty_string('Appointment time', 3)
    def __init__(self, patient, doctor, appt_time):
        self.patient = patient
        self.doctor = doctor
        self.appt_time = appt_time


class Virtual(Appointment):
    @not_empty_string('Appointment time', 3)
    def __init__(self, patient, doctor, appt_time):
        self.patient = patient
        self.doctor = doctor
        self.appt_time = appt_time
