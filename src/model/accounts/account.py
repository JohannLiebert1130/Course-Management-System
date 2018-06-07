import pymysql

from src.common.database import Database
from src.common.utils import Utils
from src.model.admins.admin import Admin
from src.model.students.student import Student
from src.model.teachers.teacher import Teacher
from src.model.users.user import User


class Account:
    def __init__(self, user_id, password, user_type, school):
        self.user_id = user_id
        self.password = password
        self.user_type = user_type
        self.school = school

    def __str__(self):
        return f"user ID:{self.user_id}\nuser type:{self.user_type}"

    @staticmethod
    def is_valid_login(user_id, password):
        """
        This method verifies that an user_id/password combo is valid or not.
        Check that the user ID exists, and that the password associated to that ID is valid.
        :param user_id: The user's ID
        :param password: A sha512 hashed password
        :return: (login state, user)
        """

        Database.initialize()

        sql = """
        SELECT * FROM accounts
        WHERE user_id = (%s)
        """
        account_data = Database.query(sql, user_id)  # password in sha512->pbkdf2_sha512

        if account_data:
            account_data = account_data[0]
            password_from_db = account_data[1]

            if Utils.check_hashed_password(password, user_id, password_from_db):
                print("login successfully!")
                user_type = account_data[2]
                user = Account.get_corresponding_user(user_id, user_type)

                Database.close()
                return 1, user
            else:
                print("invalid password!")
                Database.close()
                return -1, None
        else:
            print("This account do not exist!")
            Database.close()
            return -2, None

    @staticmethod
    def create_account(user_id, password, user_type, school):
        """
        This method registers a user using user id and password.
        The password already comes hashed as sha-512.
        :param user_id: user's id (might be invalid)
        :param password: user's password in plain text
        :param user_type: user's type (can be admin, teacher, or student)
        :return:
        """
        sql = """
              SELECT * FROM accounts
              WHERE user_id = (%s)
              """
        user_data = Database.query(sql, user_id)

        if user_data:
            # Tell user they are already registered
            raise ValueError("The user id you used to register already exists.")
        if not User.is_valid_user_id(user_id, user_type):
            raise ValueError('Invalid user id!')

        try:
            Account(user_id, Utils.hash_password(password, user_id), user_type, school).save_to_db()
        except pymysql.Error as error:
            raise error

    @staticmethod
    def create_accounts(accounts_data):
        Database.initialize()
        for account_data in accounts_data:
            Account.create_account(*account_data)
        Database.close()

    @staticmethod
    def read_account(user_id):
        sql = """
                      SELECT * FROM accounts
                      WHERE user_id = %s
                    """

        account_data = Database.query(sql, user_id)
        if account_data:
            account_data = account_data[0]
            return Account(*account_data)
        else:
            print("Account do not exist!")
            return None

    @staticmethod
    def read_accounts(school, account_type):
        Database.initialize()

        sql = f"SELECT * FROM accounts WHERE school='{school}'"
        if account_type is not None:
            sql += f" and user_type = {account_type}"
        print(sql)
        accounts_data = Database.query(sql)

        Database.close()

        if accounts_data:
            for account_data in accounts_data:
                account_data = list(account_data)
                account_data[2] = str(account_data[2])
                yield account_data

    @staticmethod
    def modify_account(user_id, password, user_type, school):
        sql = """
              SELECT * FROM accounts
              WHERE user_id = (%s)
              """
        account_data = Database.query(sql, user_id)

        if account_data:
            Account(user_id, Utils.hash_password(password, user_id), user_type, school).save_to_db()
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
            INSERT INTO accounts(user_id, password, user_type, school)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE password = %s, user_type = %s, school = %s
            """

        Database.data_handle(sql, *self.to_list())

    def to_list(self):
        return [self.user_id, self.password, self.user_type, self.school, self.password, self.user_type, self.school]

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






