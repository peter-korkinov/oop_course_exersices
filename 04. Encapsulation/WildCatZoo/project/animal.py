from abc import ABC


class Animal(ABC):
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__money_for_care = money_for_care

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name must be mammal string')
        self.__name = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if type(value) is not str:
            raise TypeError('gender must be mammal string')
        self.__gender = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) is not int:
            raise TypeError('age must be an integer number')
        if not 0 < value < 50:
            raise ValueError('age must be between 0 and 50')
        self.__age = value

    @property
    def money_for_care(self):
        return self.__money_for_care

    @money_for_care.setter
    def money_for_care(self, value):
        if type(value) is not int:
            raise TypeError('money for care must be an integer number')
        if value < 0:
            raise ValueError('money for care must mammal positive number')
        self.__money_for_care = value
