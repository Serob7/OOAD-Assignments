from abc import ABC, abstractmethod

class Operatoins(ABC):
    @abstractmethod
    def schedule_appt(self, doctor, appt_time):
        ...
    def view_history(self):
        print(f"\t{self.name}'s medical history")
        for history in self.medical_history:
            print(history)
