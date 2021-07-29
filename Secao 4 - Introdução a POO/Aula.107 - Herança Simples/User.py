class User:

    def __init__(self, name, email, code_id):
        self.name = name
        self.__email = email
        self.__code_id = code_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.title()
        self.__name = value

    # TASK -> regex
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def code_id(self):
        return self.__code_id

    @code_id.setter
    def code_id(self, value):
        self.__code_id = value
