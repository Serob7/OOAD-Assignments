from validators import not_empty_string, email_checker
from course import UndergraduateCourse, GraduateCourse

class Professor:
    @not_empty_string('Name', 1)
    @email_checker('Contact', 2)
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.tought_courses = []

    def create_undergraduate_course(self, name, content):
        course = UndergraduateCourse(name, self, content)
        self.tought_courses.append(course)
        return course

    def create_graduate_course(self, name, content):
        course = GraduateCourse(name, self, content)
        self.tought_courses.append(course)
        return course

