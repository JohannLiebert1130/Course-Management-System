from src.common.database import Database
from src.model.users.user import User


class Teacher(User):
    def __init__(self, user_id, user_type, name, p_id, folk=None, political_status=None,
                 school=None, position=None, phone=None):
        super().__init__(user_id, user_type, name, p_id, folk, political_status, phone)
        self.school = school
        self.position = position

    @staticmethod
    def create_teacher(user_id, user_type, name, p_id, folk=None, political_status=None,
                 school=None, position=None, phone=None):
        sql = """
              SELECT * FROM teachers
              WHERE user_id = (%s)
            """
        user_data = Database.query(sql, user_id)

        if user_data:
            # Tell user they are already registered
            print("The user id you used to register already exists.")
            return False
        if not User.is_valid_user_id(user_id, user_type):
            return False

        Teacher(user_id, user_type, name, p_id, folk, political_status, school, position, phone).save_to_db()
        return True

    def save_to_db(self):
        sql = """
            INSERT INTO teachers(user_id, user_type, name, p_id, gender, birthday, birth_place, folk,
             political_status, school, position, phone)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE folk = %s, political_status = %s, 
            school = %s, position = %s, phone = %s
            """

        Database.data_handle(sql, self.user_id, self.user_type, self.name, self.p_id, self.gender, self.birthday,
                             self.birth_place, self.folk, self.political_status, self.school, self.position, self.phone,
                             self.folk, self.political_status, self.school, self.position, self.phone)
