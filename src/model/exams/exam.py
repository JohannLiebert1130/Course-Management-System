import pymysql

from src.common.database import Database


class Exam:
    def __init__(self, course_id, course_name, year, semester, exam_time=None,
                 exam_location=None):
        self.course_id = course_id
        self.course_name = course_name
        self.exam_time = exam_time
        self.exam_location = exam_location
        self.year = year
        self.semester = semester

    @staticmethod
    def create_exam(course_id, course_name, year, semester, exam_time=None,
                    exam_location=None):
        sql = 'SELECT * FROM exams WHERE course_id = %s AND year = %s AND semester = %s'
        course_data = Database.query(sql, course_id, year, semester)

        if course_data:
            raise ValueError('The course id you used to register already exists.')

        try:
            Exam(course_id, course_name, year, semester, exam_time,
                 exam_location).save_to_db()
        except pymysql.Error as error:
            raise error

    @staticmethod
    def read_exams(teacher_id, year, semester):
        Database.initialize()

        sql = f"""select * from exams where course_id in 
        (select course_id from courses where teacher_id = '{teacher_id}') 
         and year = '{year}'"""
        if semester != ' ':
            sql += f"and semester = {semester}"

        exams_data = Database.query(sql)
        Database.close()

        if exams_data:
            for exam_data in exams_data:
                exam_data = list(exam_data)
                data = list()
                data.extend(exam_data[1:3])
                data.extend(exam_data[5:])
                yield data


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




