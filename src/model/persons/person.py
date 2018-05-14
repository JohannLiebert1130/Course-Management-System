from src.common.ChineseIDValidator.chinese_id import ChineseID


class Person:
    def __init__(self, user_id, name, p_id, folk=None, political_status=None, phone=None):
        self.user_id = user_id
        self.name = name
        self.p_id = p_id
        self.folk = folk
        self.political_status = political_status
        self.phone = phone

        chinese_id = ChineseID(self.p_id)

        self.birth_place, self.birthday, self.gender = chinese_id.get_id_details().values()

    def __str__(self):
        return f'User ID: {self.user_id}\nName: {self.name}\nID: {self.p_id}\n' \
               f'Birth place: {self.birth_place}\nBirthday: {self.birthday}\n' \
               f'Gender: {self.gender}'

