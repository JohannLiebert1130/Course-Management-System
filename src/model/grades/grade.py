import pymysql

from src.common.database import Database
from src.model.students.student import Student


def get_students_data(course_key):
    Database.initialize()

    sql = 'select * from grades where course_key= %s'
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
              update grades set grade = %s
              where grades.course_key=(SELECT id FROM courses WHERE course_id = %s) and
	          grades.student_key=(SELECT id FROM students WHERE user_id = %s)
        """
    try:
        Database.data_handle(sql, grade, course_id, student_id)
    except pymysql.Error as error:
        raise error


def save_grades(course_ids, student_ids, grades):
    Database.initialize()

    sql = """
              update grades set grade = %s
              where grades.course_key=(SELECT id FROM courses WHERE course_id = %s) and
	          grades.student_key=(SELECT id FROM students WHERE user_id = %s)
            """
    try:
        for course_id, student_id, grade in zip(course_ids, student_ids, grades):
            Database.data_handle(sql, course_id, student_id, grade)
    except pymysql.Error as error:
        raise error
    finally:
        Database.close()


def read_grades(query_key, data):
    if query_key == 'Course ID':
        sql = """select name, user_id, class,grade from students inner join grades where 
                (students.id,grade) in (select student_key, grade from grades where course_key =
                 (select id from courses where course_id = %s))

              """
    else:
        sql = """select name, user_id, class,grade from students inner join grades where user_id = %s and grade = 
                      """
    try:
        data = Database.query(sql, data)
    except pymysql.Error as error:
        raise error
    else:
        for row in data:
            sql = None


