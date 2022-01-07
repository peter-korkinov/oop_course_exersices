from abc import ABC


class Worker(ABC):
    def __init__(self, name: str, age: int, salary: int):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name must be a string')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) is not int:
            raise TypeError('age must be an integer number')
        if 0 > value > 150:
            raise ValueError('age must be between 0 and 150')
        self.__age = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if type(value) is not int:
            raise TypeError('Salary must be an integer number')
        if value <= 0:
            raise ValueError('salary must be a positive number')
        self.__salary = value
