import re
from src.common.ChineseIDValidator.addr_code_crawler import AddressCode
from src.common.utils import Utils


class ChineseID:
    address_code_url = 'http://www.mca.gov.cn/article/sj/xzqh//1980/'
    addr_code_dic = AddressCode.read_addr_code_from_local()
    addr_code_1995_dic = AddressCode.read_addr_code_from_local('1995_addr_codes.json')

    def __init__(self, id_str):

        self.id_str = id_str

        if not self.is_valid_length():
            raise ValueError("invalid ID length!")

        self.address_code = id_str[:6]
        self.birth_date_code = id_str[6:14]
        self.sequence_code = id_str[14:17]
        self.check_code = id_str[17]

        if not self.is_valid_id():
            raise ValueError("invalid official ID!")

    def __str__(self):
        return f"Address code:{self.address_code}\nBirth date code:{self.birth_date_code}\nsequence code:" \
               f"{self.sequence_code}\ncheck code:{self.check_code}"

    @staticmethod
    def set_address_code_url(url):
        ChineseID.address_code_url = url

    def is_valid_length(self):
        if self.id_str is None:
            return False
        elif len(self.id_str) == 18:
            return True
        else:
            return False

    def is_valid_addr_code(self):

        if self.address_code in ChineseID.addr_code_dic:
            return True
        elif self.address_code in ChineseID.addr_code_1995_dic:
            return True
        else:
            return False

    def is_valid_birth_date(self):
        return Utils.is_valid_date(self.birth_date_code)

    def is_valid_sequence_code(self):
        p = re.compile(r'\d\d\d$')
        if p.match(self.sequence_code) is not None:
            return True
        else:
            return False

    def is_valid_check_code(self):
        sum = 0
        for i in range(17):
            sum += ((1 << (17 - i)) % 11) * int(self.id_str[i])

        n = (12 - (sum % 11)) % 11

        if n < 10:
            return n == int(self.id_str[17])
        else:
            return self.id_str[17] == 'X'

    def is_valid_id(self):
        # print(f'is valid length: {self.is_valid_length()}\n'
        #       f'is valid address: {self.is_valid_addr_code()}\n'
        #       f'is valid birth: {self.is_valid_birth_date()}\n'
        #       f'is valid sequence code: {self.is_valid_sequence_code()}\n'
        #       f'is valid check code: {self.is_valid_check_code()}')
        if self.is_valid_length() and self.is_valid_addr_code() and self.is_valid_birth_date() \
                and self.is_valid_sequence_code() and self.is_valid_check_code():
            return True
        else:
            return False

    def get_address_details(self):
        """
        Supposes this ID is valid, the function will get the ID's address information in details.
        :return: a string which contain the ID owner's birth place.
        """
        if self.address_code in ChineseID.addr_code_dic:
            dic = ChineseID.addr_code_dic
        else:
            dic = ChineseID.addr_code_1995_dic

        birth_place = dic[self.address_code]
        if self.address_code[-2:] != '00':
            birth_place = dic[self.address_code[:-2]+'00'] + birth_place
        if self.address_code[2:4] != '00':
            birth_place = dic[self.address_code[:2]+'0000'] + birth_place

        return birth_place

    def get_id_details(self):
        """
        Suppose this ID is valid, the function will get the ID's information in details.
        :return: a Python dict which contain the ID owner's birth place, birthday and gender.
        """
        birth_place = self.get_address_details()
        birthday = self.birth_date_code[:4] + '-' + self.birth_date_code[4:6] + '-' + self.birth_date_code[6:]
        gender = 'Male' if int(self.sequence_code[-1]) % 2 == 1 else 'Female'

        details = {'Birth place': birth_place,
                   'Birthday': birthday,
                   'Gender': gender}

        return details
