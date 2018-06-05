from src.common.database import Database
from src.model.students.student import Student


def get_students_data(course_key):
    Database.initialize()

    sql = 'select * from student_courses where course_id= %s'
    data = Database.query(sql, course_key)
    print(data)

    students_data = list()
    for row in data:
        student_key = row[1]
        temp = Student.read_student(student_key)
        student_data = list()
        student_data.append(temp[2])
        student_data.append(temp[1])
        student_data.append(temp[9])
        student_data.append(temp[11])
        student_data.append(temp[12])
        students_data.append(student_data)

    return students_data
