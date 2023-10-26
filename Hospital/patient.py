from validators import not_empty_string, positive_integer_checker

class Patient:
    @not_empty_string('Name', 1)
    @positive_integer_checker('Age', 2)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.medical_history = []

