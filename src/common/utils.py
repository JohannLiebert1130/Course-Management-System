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

    @staticmethod
    def user_id_is_valid(user_id, user_type):

        if user_type == 0:
            # an admin type
            pattern = re.compile('A\d{3}$')
        elif user_type == 1:
            # an teacher type
            pattern = re.compile('\d{8}$')
        elif user_type == 2:
            # an student type
            pattern = re.compile('\d{13}$')
        else:
            print("invalid user type!")
            return False

        if pattern.match(user_id):
            return True
        else:
            print("The user id does not have the right format.")
            return False


if __name__ == '__main__':
    hashed_pw = Utils.hash_password('fuck', 'shit')
    print(len(hashed_pw))
    print(Utils.check_hashed_password('fuck', 'shit', hashed_pw))

    print()

    print(Utils.user_id_is_valid('2013209620013', 3))
    print(Utils.user_id_is_valid('2013209620013', 2))
    print(Utils.user_id_is_valid('2013209620013', 1))
