import re

from passlib.hash import pbkdf2_sha512


class Utils(object):
    @staticmethod
    def hash_password(password, user_id):
        """
        Hashes a password using pbkdf2_sha512
        :param password:
        :param user_id:
        :return: A pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.hash(password+user_id)

    @staticmethod
    def check_hashed_password(password, user_id, hashed_password):
        """
        Checks that the password the user sent matches that of the database.
        The database password is encrypted more than the user's password at this stage.
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: true if passwords match, false otherwise
        """
        print(password + user_id)
        return pbkdf2_sha512.verify(password + user_id, hashed_password)


if __name__ == '__main__':
    hashed_pw = Utils.hash_password('fuck', 'shit')
    print(len(hashed_pw))
    print(Utils.check_hashed_password('fuck', 'shit', hashed_pw))
