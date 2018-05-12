from common.database import Database
from common.utils import Utils


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
        user_data = Database.query(sql, user_id)  # password in sha512->pbkdf2_sha512

        Database.close()

        print(user_data)

        if user_data:
            password_from_db = user_data[0][2]

            if Utils.check_hashed_password(password, user_id, password_from_db):
                print("login successfully!")
                user_type = int(user_data[0][3])
                return True, user_type
            else:
                print("invalid password!")
                return False, -1
        else:
            print("This user do not exist!")
            return False, -1

    @staticmethod
    def register_user(user_id, password, user_type):
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
        if not Utils.user_id_is_valid(user_id, user_type):
            return False

        Account(user_id, Utils.hash_password(password, user_id), user_type).save_to_db()
        return True

    def save_to_db(self):
        sql = """
            INSERT INTO accounts(user_id, password, user_type)
            VALUES (%s, %s, %s)
            """

        Database.data_handle(sql, self.user_id, self.password, self.user_type)


if __name__ == '__main__':
    Database.initialize()
    Account.is_valid_login('test_id', 'test_pw')

    Account.register_user(user_id='cs2015001', password='fuck', user_type=2)
    Account.register_user(user_id='2015335820024', password='fuck', user_type=2)
    Database.close()
