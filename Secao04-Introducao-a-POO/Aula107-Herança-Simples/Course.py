from User import User


class Course:
    def __init__(self, name, duration=2):
        self.__name = name
        self.__duration = duration


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value
