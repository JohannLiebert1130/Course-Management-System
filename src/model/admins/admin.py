import pymysql

from src.common.database import Database
from src.model.users.user import User


class Admin(User):
    def __init__(self, user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                 folk=None, political_status=None, school=None, phone=None):
        super().__init__(user_id, 0, name, p_id, gender, birthday, birth_place, folk,
                         political_status, school, phone)

    @staticmethod
    def create_admin(user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                     folk=None, political_status=None, school=None, phone=None):

        admin = Admin(user_id, name, p_id, gender, birthday, birth_place, folk,
                      political_status, school, phone)

        if p_id is None:
            sql = """
                  SELECT * FROM admins
                  WHERE user_id = %s
                  """
            user_data = Database.query(sql, admin.user_id)
        else:
            sql = """
                  SELECT * FROM admins
                  WHERE user_id = %s OR p_id = %s
                  """
            user_data = Database.query(sql, admin.user_id, admin.p_id)

        if user_data:
            # Tell user they are already registered
            raise ValueError('The user id you used to register already exists.')

        try:
            admin.save_to_db()
        except pymysql.Error as error:
            raise error

    @staticmethod
    def read_admin(user_id):
        sql = """
                  SELECT * FROM admins
                  WHERE user_id = %s
                """

        user_data = Database.query(sql, user_id)

        if user_data:
            user_data = list(user_data[0])
            user_data[5] = str(user_data[5])
            return Admin(*user_data)
        else:
            print("user do not exist!")
            return None

    @staticmethod
    def modify_admin(user_id, name, p_id=None, gender=None, birthday=None, birth_place=None,
                     folk=None, political_status=None, school=None, phone=None):

        sql = """
                  SELECT * FROM admins
                  WHERE user_id = %s
                """
        user_data = Database.query(sql, user_id)

        if user_data:
            Admin(user_id, name, p_id, gender, birthday, birth_place, folk,
                  political_status, school, phone).save_to_db()
            return True
        else:
            return False

    @staticmethod
    def delete_admin(user_id):
        sql = """
                      DELETE FROM admins 
                      WHERE user_id = (%s)
                      """
        try:
            Database.data_handle(sql, user_id)
        except:
            print('Delete admin failed!')
            return False
        else:
            return True

    def save_to_db(self):
        sql = """
                INSERT INTO admins(user_id, name, p_id, gender, birthday, birth_place, folk,
                 political_status, school, phone)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE name = %s, p_id = %s, gender = %s, birthday = %s,
                birth_place = %s, folk = %s, political_status = %s, school = %s, phone = %s
                """

        Database.data_handle(sql, *self.to_list())

    def to_list(self):
        return [self.user_id, self.name, self.p_id, self.gender, self.birthday,
                self.birth_place, self.folk, self.political_status, self.school, self.phone,
                self.name, self.p_id, self.gender, self.birthday, self.birth_place, self.folk, self.political_status,
                self.school, self.phone]


