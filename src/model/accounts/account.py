from src.common.database import Database
from src.common.utils import Utils
from src.model.admins.admin import Admin
from src.model.students.student import Student
from src.model.teachers.teacher import Teacher
from src.model.users.user import User


class Account:
    def __init__(self, user_id, password, user_type):
        self.user_id = user_id
        self.password = password
        self.user_type = user_type

    def __str__(self):
        return f"user ID:{self.user_id}\nuser type:{self.user_type}"

    @staticmethod
    def is_valid_login(user_id, password):
        """
        This method verifies that an user_id/password combo is valid or not.
        Check that the user ID exists, and that the password associated to that ID is valid.
        :param user_id: The user's ID
        :param password: A sha512 hashed password
        :return: (True, user_type) if valid, (False, -1) otherwise
        """

        Database.initialize()

        sql = """
        SELECT * FROM accounts
        WHERE user_id = (%s)
        """
        account_data = Database.query(sql, user_id)  # password in sha512->pbkdf2_sha512

        if account_data:
            account_data = account_data[0]
            password_from_db = account_data[2]

            if Utils.check_hashed_password(password, user_id, password_from_db):
                print("login successfully!")
                user_type = account_data[3]
                user = Account.get_corresponding_user(user_id, user_type)

                Database.close()
                return True, user
            else:
                print("invalid password!")
                Database.close()
                return False, None
        else:
            print("This account do not exist!")
            Database.close()
            return False, None

    @staticmethod
    def create_account(user_id, password, user_type):
        """
        This method registers a user using user id and password.
        The password already comes hashed as sha-512.
        :param user_id: user's id (might be invalid)
        :param password: user's password in plain text
        :param user_type: user's type (can be admin, teacher, or student)
        :return: True if registered successfully, or False otherwise (exceptions can also be raised)
        """
        sql = """
              SELECT * FROM accounts
              WHERE user_id = (%s)
              """
        user_data = Database.query(sql, user_id)

        if user_data:
            # Tell user they are already registered
            print("The user id you used to register already exists.")
            return False
        if not User.is_valid_user_id(user_id, user_type):
            return False

        Account(user_id, Utils.hash_password(password, user_id), user_type).save_to_db()
        return True

    @staticmethod
    def modify_account(user_id, password, user_type):
        sql = """
              SELECT * FROM accounts
              WHERE user_id = (%s)
              """
        user_data = Database.query(sql, user_id)

        if user_data:
            Account(user_id, Utils.hash_password(password, user_id), user_type).save_to_db()
            return True
        else:
            return False

    @staticmethod
    def delete_account(user_id):
        sql = """
              DELETE FROM accounts 
              WHERE user_id = (%s)
              """
        try:
            Database.data_handle(sql, user_id)
        except:
            print('Delete account failed!')
            return False
        else:
            return True

    def save_to_db(self):
        sql = """
            REPLACE INTO accounts(user_id, password, user_type)
            VALUES (%s, %s, %s)
            """

        Database.data_handle(sql, self.user_id, self.password, self.user_type)

    @staticmethod
    def get_corresponding_user(user_id, user_type):
        print(f'get_corresponding_user: user_id={user_id} user_type={user_type}')
        try:
            if user_type == 0:
                return Admin.read_admin(user_id)
            elif user_type == 1:
                return Teacher.read_teacher(user_id)
            elif user_type == 2:
                return Student.read_student(user_id)
        except:
            print('User not founded!')






