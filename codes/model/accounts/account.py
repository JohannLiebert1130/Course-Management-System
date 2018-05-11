import uuid
from common.database import Database
from common.utils import Utils


class Account:
    def __init__(self, user_id, password, _id=None):
        self.user_id = user_id
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __str__(self):
        return f"user ID:{self.user_id}"

    @staticmethod
    def is_valid_login(user_id, password):
        """
        This method verifies that an user_id/password combo is valid or not.
        Check that the user ID exists, and that the password associated to that ID is valid.
        :param user_id: The user's ID
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """
        sql = """
        SELECT * FROM accounts
        WHERE user_id = (%s)
        """
        user_data = Database.query(sql, user_id)  # password in sha512->pbkdf2_sha512
        print(user_data)

        if user_data:
            password_from_db = user_data[0][2]

            if Utils.check_hashed_password(password, user_id, password_from_db):
                print("login successfully!")
                return True
            else:
                print("invalid password!")
                return False
        else:
            print("user data it's empty!")
            return False


if __name__ == '__main__':
    Database.initialize()
    Account.is_valid_login('test_id', 'test_pw')
