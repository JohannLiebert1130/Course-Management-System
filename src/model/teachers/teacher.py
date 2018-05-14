class Person(object):
    pass


class Teacher(Person):
    def __init__(self, user_id, user_type, name, p_id, folk=None, political_status=None,
                 school=None, position=None, phone=None):
        super.__init__(user_id, user_type, name, p_id, folk, political_status, phone)
        self.school = school
        self.position = position

