from datetime import datetime
from User import User


class Subscribed(User):
    def __init__(self, name, email, code_id, fone):
        User.__init__(self, name, email, code_id)
        self.__fone = fone
        self.__period = datetime.strftime(datetime.now(), '%d-%m-%Y')

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value):
        self.__period = value

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, value):
        self.__fone = value
