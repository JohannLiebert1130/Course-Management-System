import pymysql

from src.common.database import Database
from src.common.utils import Utils
from src.model.students.student import Student


class Grade:

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def read_grades(query_key, data):
        if not Utils.check_whitespace(data):
            if query_key == 'Course ID':
                sql = f"""
                select course_name, courses.course_id, user_id, name, students.school, grade 
                from students, courses, grades
                where (user_id,grade) in  (select student_id,grade from grades where course_id ={data} )
                 and courses.course_id = {data}
    
                      """
            else:
                sql = f"""
                select course_name, courses.course_id, user_id, name, students.school, grade 
                from students, courses, grades
                where (courses.course_id, grade) in  
                (select course_id,grade from grades where student_id = '{data}' ) 
                 and students.user_id = '{data}'
    
                    """
            try:
                Database.initialize()
                grades_data = Database.query(sql)
                return grades_data
            except pymysql.Error as error:
                raise error
            finally:
                Database.close()

        else:
            raise ValueError('Please input data!')




