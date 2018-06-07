import pymysql

from src.common.database import Database
from src.common.utils import Utils


class Grade:

    @staticmethod
    def save_grade(course_id, student_id, grade):
        sql = """
                  update grades set grade = %s
                  where course_id = %s and student_id = %s
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
                  where course_id = %s and student_id = %s
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




