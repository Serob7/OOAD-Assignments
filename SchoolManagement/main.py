from course import Math, English
from student import Student
from teacher import Teacher

def main():

    #creating Teacher instance
    teacher = Teacher('John', 'john@gmail.com', 'Math and English')

    #professor creating courses
    course1 = teacher.create_math_course('Geometry')
    course2 = teacher.create_english_course('Passive Voice')


    # create Student instance, enroll in courses, , view progress
    student = Student('Serob', 'serob@gmail.com')
    student.enroll_course(course1)
    student.enroll_course(course2)
    student.view_progress()

if __name__ == '__main__':
    main()