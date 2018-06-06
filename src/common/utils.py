import datetime
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
        return pbkdf2_sha512.verify(password + user_id, hashed_password)

    @staticmethod
    def represents_int(s):
        try:
            int(s)
            return True
        except:
            return False

    @staticmethod
    def is_valid_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y%m%d')
        except:
            print("Incorrect data format, should be YYYYMMDD")
            return False
        else:
            return True

    @staticmethod
    def create_year_generator():
        now = datetime.datetime.now()
        count = now.year - 2010
        for i in range(count + 1):
            yield f'{2010+i}-{2010+i+1}'

    @staticmethod
    def check_whitespace(str):
        pattern = re.compile(r'\s*$')
        return pattern.match(str)

    @staticmethod
    def check_qt_item(item):
        if item is None or Utils.check_whitespace(item.text()):
            return False
        else:
            return True


if __name__ == '__main__':
    hashed_pw = Utils.hash_password('fuck', 'shit')
    print(len(hashed_pw))
    print(Utils.check_hashed_password('fuck', 'shit', hashed_pw))
    print(Utils.check_whitespace(' a'))
