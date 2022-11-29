class Card():
    def __init__(self,number,face):
        self.__number = number
        self.__face = face

    def get_number(self):
        return self.__number

    def get_face(self):
        return self.__face

    def __str__(self):
        return f'{self.__number} of {self.__face}'



