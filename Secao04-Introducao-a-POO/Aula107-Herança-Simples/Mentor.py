from datetime import datetime

from User import User


class Mentor(User):
    def __init__(self, name, email, code_id, state='', city=''):
        User.__init__(self, name, email, code_id)
        self.__state = state
        self.__city = city
        self.__date = datetime.strftime(datetime.now(), '%d-%m-%Y')

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
