import pymysql

from src.common.database import Database
from src.model.users.user import User


class Student(User):
    def __init__(self, user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                 folk=None, political_status=None, school=None, department=None, class_=None, phone=None):
        super().__init__(user_id, 2, name, p_id, gender, birthday, birth_place, folk,
                         political_status, school, phone)
        self.department = department
        self.class_ = class_

    @staticmethod
    def create_student(user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                       folk=None, political_status=None, school=None, department=None, class_=None, phone=None):

        sql = """
                  SELECT * FROM students
                  WHERE user_id = %s
                """
        user_data = Database.query(sql, user_id)

        if user_data:
            # Tell user they are already registered
            raise ValueError('The user id you used to register already exists.')

        try:
            Student(user_id, name, p_id, gender, birthday, birth_place, folk, political_status,
                    school, department, class_, phone).save_to_db()
        except pymysql.Error as error:
            raise error

    @staticmethod
    def read_student(student_key):
        sql = """
                  SELECT * FROM students
                  WHERE id = %s
                """

        user_data = Database.query(sql, student_key)

        if user_data:
            user_data = list(user_data[0])
            user_data[5] = str(user_data[5])

            return user_data
        else:
            print("user do not exist!")
            return None

    @staticmethod
    def read_students(school, department=None, class_name=None, student_id=None, student_name=None):
        Database.initialize()

        sql = f"SELECT * FROM students WHERE POSITION('{school}' in school)"
        if department:
            sql += f" and POSITION('{department}' in department)"
        if class_name:
            sql += f" and POSITION('{class_name}' in class)"
        if student_id:
            sql += f" and POSITION('{student_id}' in user_id)"
        if student_name:
            sql += f" and POSITION('{student_name}' in name)"

        users_data = Database.query(sql)
        Database.close()

        if users_data:
            for user_data in users_data:
                user_data = list(user_data)

                birthday = user_data[4]
                if birthday is not None:
                    user_data[4] = str(birthday)

                yield user_data

    @staticmethod
    def modify_student(user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                       folk=None, political_status=None, school=None, department=None, class_=None, phone=None):

        sql = """
                  SELECT * FROM students
                  WHERE user_id = %s
                """
        user_data = Database.query(sql, user_id)

        if user_data:
            try:
                Student(user_id, name, p_id, gender, birthday, birth_place, folk, political_status,
                        school, department, class_, phone).save_to_db()
            except pymysql.Error as error:
                raise error
        else:
            raise ValueError('Student do not exist!')

    @staticmethod
    def delete_student(user_id):
        Database.initialize()
        sql = """
              DELETE FROM students 
              WHERE user_id = (%s)
            """
        try:
            Database.data_handle(sql, user_id)
        except:
            print('Delete student failed!')
            return False
        else:
            return True
        finally:
            Database.close()

    def save_to_db(self):
        sql = """
                INSERT INTO students(user_id, name, p_id, gender, birthday, birth_place, folk,
                 political_status, school, department, class, phone)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE name = %s, p_id = %s, gender = %s, birthday = %s, birth_place = %s,
                folk = %s, political_status = %s, school = %s, department = %s, class = %s, phone = %s
                """

        Database.data_handle(sql, *self.to_list())

    def to_list(self):
        return [self.user_id, self.name, self.p_id, self.gender, self.birthday, self.birth_place,
                self.folk, self.political_status, self.school, self.department, self.class_, self.phone,
                self.name, self.p_id, self.gender, self.birthday, self.birth_place, self.folk, self.political_status,
                self.school, self.department, self.class_, self.phone]


if __name__ == '__main__':
    for i in Student.read_all_students():
        print(i)