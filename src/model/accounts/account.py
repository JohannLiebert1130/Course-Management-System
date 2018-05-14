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
        account_data = Database.query(sql, user_id)[0]  # password in sha512->pbkdf2_sha512

        Database.close()

        print(account_data)

        if account_data:
            password_from_db = account_data[2]

            if Utils.check_hashed_password(password, user_id, password_from_db):
                print("login successfully!")

                user = User.get_user_by_user_id(user_id)
                return True, user
            else:
                print("invalid password!")
                return False, None
        else:
            print("This user do not exist!")
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
        if user_type == 0:
            table_name = 'admins'
        elif user_type == 1:
            table_name = 'teachers'
        elif user_type == 2:
            table_name = 'students'
        else:
            raise Exception('Invalid user type')

        Database.initialize()

        sql = "SELECT * FROM " + table_name + " WHERE user_id = %s"

        data = list(Database.query(sql, user_id)[0])
        data[6] = str(data[6])
        user_data = [data[1]]
        user_data.extend(data[3:])

        Database.close()

        if user_type == 0:
            user = Admin(*user_data)
        elif user_type == 1:
            user = Teacher(*user_data)
        elif user_type == 2:
            user = Student(*user_data)

        return user




