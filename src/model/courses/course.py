import pymysql

from src.common.database import Database


class Course:
    def __init__(self, course_id, course_name, school=None, teacher_name=None, class_time=None,
                 location=None, year=None,semester=None):
        self.course_id = course_id
        self.course_name = course_name
        self.school = school
        self.teacher_name = teacher_name
        self.class_time = class_time
        self.location = location
        self.year = year
        self.semester = semester

    @staticmethod
    def create_course(course_id, course_name, school=None, teacher_name=None, class_time=None,
                      location=None, year=None, semester=None):
        sql = 'SELECT * FROM courses WHERE course_id = %s'
        course_data = Database.query(sql, course_id)

        if course_data:
            raise ValueError('The course id you used to register already exists.')

        Course(course_id, course_name, school, teacher_name,
               class_time, location, year, semester).save_to_db()

    @staticmethod
    def read_course(course_id):
        sql = """
                  SELECT * FROM courses
                  WHERE course_id = %s
                """

        course_data = Database.query(sql, course_id)

        if course_data:
            course_data = list(course_data[0])
            course_data = course_data[1:]

            return Course(*course_data)
        else:
            print("course do not exist!")
            return None

    @staticmethod
    def read_courses(school):
        Database.initialize()

        sql = "SELECT * FROM courses WHERE school = %s"
        courses_data = Database.query(sql, school)

        Database.close()

        if courses_data:
            for course_data in courses_data:
                course_data = list(course_data)
                course_data = course_data[1:]
                yield course_data

    @staticmethod
    def modify_course(course_id, course_name, school=None, teacher_name=None, class_time=None,
                      location=None, year=None, semester=None):

        sql = """
                  SELECT * FROM courses
                  WHERE course_id = %s
                """
        course_data = Database.query(sql, course_id)

        if course_data:
            Course(course_id, course_name, school, teacher_name,
                   class_time, location, year, semester).save_to_db()
            return True
        else:
            return False

    @staticmethod
    def delete_course(course_id):
        Database.initialize()
        sql = "DELETE FROM courses WHERE course_id = %s"

        try:
            Database.data_handle(sql, course_id)
        except pymysql.Error:
            print('Delete course failed!')
            return False
        else:
            return True
        finally:
            Database.close()

    def save_to_db(self):
        sql = """
                INSERT INTO courses(course_id, course_name, school, teacher_name,
                                    class_time, location, year, semester)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE course_name = %s, school = %s, teacher_name = %s, class_time = %s,
                location = %s, year = %s, semester = %s
            """

        Database.data_handle(sql, *self.to_list())

    def to_list(self):
        return [self.course_id, self.course_name, self.school, self.teacher_name, self.class_time,
                self.location, self.year, self.semester, self.course_name, self.school, self.teacher_name, self.class_time,
                self.location, self.year, self.semester]




