import pymysql

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
        student_data.append(row[3])
        students_data.append(student_data)

    return students_data


def save_grade(course_id, student_id, grade):
    sql = """
              update student_courses set grade = %s
              where student_courses.course_id=(SELECT id FROM courses WHERE course_id = %s) and
	          student_courses.student_id=(SELECT id FROM students WHERE user_id = %s)
        """
    try:
        Database.data_handle(sql, grade, course_id, student_id)
    except pymysql.Error as error:
        raise error


def save_grades(course_ids, student_ids, grades):
    Database.initialize()

    sql = """
                  update student_courses set grade = %s
              where student_courses.course_id=(SELECT id FROM courses WHERE course_id = %s) and
	          student_courses.student_id=(SELECT id FROM students WHERE user_id = %s)
            """
    try:
        for course_id, student_id, grade in zip(course_ids, student_ids, grades):
            Database.data_handle(sql, course_id, student_id, grade)
    except pymysql.Error as error:
        raise error
    finally:
        Database.close()
