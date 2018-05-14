import re

from src.common.ChineseIDValidator.chinese_id import ChineseID


class User:
    def __init__(self, user_id, user_type, name, p_id, folk=None, political_status=None, phone=None):
        self.user_id = user_id
        self.name = name
        self.p_id = p_id
        self.user_type = user_type
        self.folk = folk
        self.political_status = political_status
        self.phone = phone

        chinese_id = ChineseID(self.p_id)

        self.birth_place, self.birthday, self.gender = chinese_id.get_id_details().values()

    def __str__(self):
        return f'User ID: {self.user_id}\nName: {self.name}\nID: {self.p_id}\n' \
               f'User Type: {self.user_type}\nBirth place: {self.birth_place}\n' \
               f'Birthday: {self.birthday}\nGender: {self.gender}'

    @staticmethod
    def is_valid_user_id(user_id, user_type):

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

