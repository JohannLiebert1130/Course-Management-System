import re

import pymysql

from src.common.database import Database
from src.model.users.user import User


class Teacher(User):
    def __init__(self, user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                 folk=None, political_status=None, school=None, position=None, phone=None):
        super().__init__(user_id, 1, name, p_id, gender, birthday, birth_place, folk,
                         political_status, school, phone)
        self.position = position

    @staticmethod
    def create_teacher(user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                       folk=None, political_status=None, school=None, position=None, phone=None):
        if re.compile('\d{18}$').match(p_id):
            sql = """
                  SELECT * FROM teachers
                  WHERE user_id = %s or p_id = %s
                """
            user_data = Database.query(sql, user_id, p_id)
        elif p_id == 'foreigner':
            sql = """
                  SELECT * FROM teachers
                  WHERE user_id = %s
                """
            user_data = Database.query(sql, user_id)
        else:
            raise ValueError('Invalid official ID.')

        print('user data', user_data)
        if user_data:
            # Tell user they are already registered
            raise ValueError('The user already exists.')
        try:
            Teacher(user_id, name, p_id, gender, birthday, birth_place, folk,
                    political_status, school, position, phone).save_to_db()
        except pymysql.Error as error:
            raise error

    @staticmethod
    def read_teacher(user_id):
        sql = """
              SELECT * FROM teachers
              WHERE user_id = %s
            """

        user_data = Database.query(sql, user_id)

        if user_data:
            user_data = list(user_data[0])
            user_data[5] = str(user_data[5])
            return Teacher(*user_data)
        else:
            print("user do not exist!")
            return None

    @staticmethod
    def read_teachers(school, teacher_id, teacher_name, position):
        Database.initialize()

        sql = f"SELECT * FROM teachers WHERE school = '{school}'"
        if teacher_id:
            sql += f" and user_id = '{teacher_id}'"
        if teacher_name:
            sql += f" and name = '{teacher_name}'"
        if position:
            sql += f" and position = '{position}'"

        print(sql)
        teachers_data = Database.query(sql)
        Database.close()

        if teachers_data:
            for teacher_data in teachers_data:
                teacher_data = list(teacher_data)

                birthday = teacher_data[4]
                if birthday is not None:
                    teacher_data[4] = str(birthday)

                yield teacher_data

    @staticmethod
    def modify_teacher(user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                       folk=None, political_status=None, school=None, position=None, phone=None):

        sql = """
              SELECT * FROM teachers
              WHERE user_id = %s
            """
        user_data = Database.query(sql, user_id)

        if user_data:
            Teacher(user_id, name, p_id, gender, birthday, birth_place, folk,
                    political_status, school, position, phone).save_to_db()
            return True
        else:
            return False

    @staticmethod
    def delete_teacher(user_id):
        Database.initialize()
        sql = """
                  DELETE FROM teachers 
                  WHERE user_id = (%s)
                  """
        try:
            Database.data_handle(sql, user_id)
        except:
            print('Delete teacher failed!')
            return False
        else:
            return True
        finally:
            Database.close()

    def save_to_db(self):
        sql = """
            INSERT INTO teachers(user_id, name, p_id, gender, birthday, birth_place, folk,
             political_status, school, position, phone)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name = %s, p_id = %s, gender = %s, birthday = %s,
            birth_place = %s, folk = %s, political_status = %s, school = %s, position = %s, phone = %s
            """

        Database.data_handle(sql, *self.to_list())

    def to_list(self):
        return [self.user_id, self.name, self.p_id, self.gender, self.birthday,
                self.birth_place, self.folk, self.political_status, self.school, self.position, self.phone,
                self.name, self.p_id, self.gender, self.birthday, self.birth_place, self.folk, self.political_status,
                self.school, self.position, self.phone]


if __name__ == '__main__':
    for i in Teacher.read_all_teachers():
        print(i)
