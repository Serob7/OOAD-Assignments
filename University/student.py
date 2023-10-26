from validators import not_empty_string, email_checker

class Student:
    @not_empty_string('Name', 1)
    @email_checker('Contact', 2)
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.courses = []
        self.progress = 0

    def enroll_course(self, course):
        course.enroll(self)

    def complete_assignment(self, assignment):
        assignment.complete(self)

    def view_progress(self):
        print(f'Progress is {self.progress}%')

