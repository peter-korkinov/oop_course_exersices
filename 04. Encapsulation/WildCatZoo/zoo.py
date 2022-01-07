from WildCatZoo.animal import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__name = name
        self.__budget = Zoo.__budget_validator(budget)
        self.__animal_capacity = Zoo.__animal_capacity_validator(animal_capacity)
        self.__workers_capacity = Zoo.__worker_capacity_validator(workers_capacity)
        self.__animals = []
        self.__workers = []

    def add_animal(self, animal, price: int):
        if self.__animal_capacity <= len(self.__animals):
            return 'Not enough space for animal'

        if price > self.__budget:
            return 'Not enough budget'

        self.__animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.name}'

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.__workers):
            return 'Not enough space for worker'

        self.__workers.append(worker)
        return f'{worker.name} the {worker.__class__.name} hired successfully'

    def fire_worker(self, worker_name):
        worker = [worker for worker in self.__workers if worker.name == worker_name][0]

        if not worker:
            return f'There is no {worker_name} in the zoo'

        self.__workers.remove(worker)
        return f'{worker_name} fired successfully'

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.__workers])

        if total_salaries > self.__budget:
            return 'You have no budget to pay your workers. They are unhappy'

        self.__budget -= total_salaries
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name must be a string')

        self.__name = value

    @staticmethod
    def __budget_validator(value):
        if type(value) is not int:
            raise TypeError('budget must be a integer number')

        if value < 0:
            raise ValueError('budget must be a positive number')

        return value

    @staticmethod
    def __animal_capacity_validator(value):
        if type(value) is not int:
            raise TypeError('animal capacity must be a integer number')

        if value < 1:
            raise ValueError('animal capacity must a positive number')

        return value

    @staticmethod
    def __worker_capacity_validator(value):
        if type(value) is not int:
            raise TypeError('worker capacity must be an integer number')

        if value < 1:
            raise ValueError('worker capacity must be a positive number')

        return value
