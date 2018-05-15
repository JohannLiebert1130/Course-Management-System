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

        sql = """
              SELECT * FROM teachers
              WHERE user_id = %s
            """
        user_data = Database.query(sql, user_id)

        if user_data:
            # Tell user they are already registered
            print("The user id you used to register already exists.")
            return False

        Teacher(user_id, name, p_id, gender, birthday, birth_place, folk,
                political_status, school, position, phone).save_to_db()
        return True

    @staticmethod
    def read_teacher(user_id):
        sql = """
              SELECT * FROM teachers
              WHERE user_id = %s
            """

        user_data = Database.query(sql, user_id)

        if user_data:
            user_data = list(user_data[0])
            user_data[6] = str(user_data[6])

            user_data = user_data[1:]

            return Teacher(*user_data)
        else:
            print("user do not exist!")
            return None

    @staticmethod
    def read_all_teachers():
        Database.initialize()

        sql = "SELECT * FROM teachers"
        users_data = Database.query(sql)

        Database.close()

        if users_data:
            for user_data in users_data:
                user_data = list(user_data)
                user_data[5] = str(user_data[5])

                user_data = user_data[1:]
                yield user_data

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
