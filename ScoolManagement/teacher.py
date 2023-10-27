from validators import not_empty_string, email_checker
from course import Math, English

class Teacher:
    @not_empty_string('Name', 1)
    @email_checker('Contact', 2)
    @not_empty_string('Subject', 3)
    def __init__(self, name, contact, subject):
        self.name = name
        self.contact = contact
        self.subject = subject

    def create_math_course(self, name):
        course = Math(name, self)
        return course

    def create_english_course(self, name):
        course = English(name, self)
        return course

    def view_student_progress(self, student):
        student.view_progress()
