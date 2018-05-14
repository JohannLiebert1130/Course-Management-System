from src.common.database import Database
from src.common.utils import Utils
from src.model.accounts.account import Account
from src.model.persons.person import Person


class Admin(Person):
    def __init__(self, user_id, name, p_id, folk=None, political_status=None, phone=None):
        Person.__init__(user_id, name, p_id, folk, political_status, phone)


