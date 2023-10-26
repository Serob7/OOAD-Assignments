from course import GraduateCourse, UndergraduateCourse
from student import Student
from professor import Professor
from assignments import TestAssignment, CodeAssignment

def main():

    #creating Professor instance
    professor = Professor('John', 'john@gmail.com')

    #professor creating courses
    course1 = professor.create_undergraduate_course('Python fundamentals', 'Python essentials')
    course2 = professor.create_graduate_course('Python OOAD', 'Learning OOAD with Python')


    #create Assignment instance
    test = TestAssignment('Python easy test')
    code = CodeAssignment('University project implementation')

    # create Student instance, enroll in courses, complete assignments, view progress
    student = Student('Serob', 'serob@gmail.com')
    student.enroll_course(course1)
    student.enroll_course(course2)
    student.complete_assignment(test)
    student.complete_assignment(code)
    student.view_progress()

if __name__ == '__main__':
    main()