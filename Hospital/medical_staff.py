from validators import not_empty_string
from medical_procedures import CheckIn, CheckOut


class MedicalStaff:
    @not_empty_string('Name', 1)
    @not_empty_string('Position', 2)

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def check_in(self, patient):
        operation = CheckIn('CheckIn')
        operation.operate(patient, self)


    def check_out(self, patient):
        operation = CheckOut('CheckOut')
        operation.operate(patient, self)

