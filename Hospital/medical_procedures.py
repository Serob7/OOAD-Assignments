from abc import ABC, abstractmethod
from validators import not_empty_string
class MedicalProcedure(ABC):
    @abstractmethod
    def perform(self,doctor, patient):
        ...



class Surgery(MedicalProcedure):
    @not_empty_string('Name', 1)
    def __init__(self, name):
        self.name = name
    def perform(self, doctor, patient):
        print(f'{doctor.name} is doing a surgery on patient {patient.name}')
        patient.medical_history.append(self)

class CheckUp(MedicalProcedure):
    @not_empty_string('Name', 1)
    def __init__(self, name):
        self.name = name
    def perform(self, doctor, patient):
        print(f'{doctor.name} is doing an {self.name} with patient {patient.name}')
        patient.medical_history.append(self)

class MedicalOperations(ABC):
    @not_empty_string('Name', 1)
    def __init__(self, name):
        self.name = name

    def operate(self, patient, medical_staff):
        ...

class CheckIn(MedicalOperations):
    def operate(self, patient, medical_staff):
        print(f'{medical_staff.name} checked in Patient {patient.name}  to our Hospital')

class CheckOut(MedicalOperations):
    def operate(self, patient, medical_staff):
        print(f'{medical_staff.name} checked out Patient {patient.name}  from our Hospital')


