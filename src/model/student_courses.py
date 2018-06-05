from src.common.database import Database
from src.model.students.student import Student


def get_students(course_key):
    Database.initialize()

    sql = 'select * from student_courses where course_id= %s'
    data = Database.query(sql, course_key)
    print(data)

    students_data = list()
    for row in data:
        student_key = row[1]
        student_data = Student.read_student(student_key)
        students_data.append(student_data)
