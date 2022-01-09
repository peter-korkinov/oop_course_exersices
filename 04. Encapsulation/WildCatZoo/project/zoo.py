class Zoo:
    ANIMAL_TYPES_IN_ZOO = ['Lion', 'Tiger', 'Cheetah']
    WORKER_POSITIONS_IN_ZOO = ['Keeper', 'Caretaker', 'Vet']

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
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.__workers):
            return 'Not enough space for worker'

        self.__workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        worker_arr = [worker for worker in self.__workers if worker.name == worker_name]

        if not worker_arr:
            return f'There is no {worker_name} in the zoo'

        self.__workers.remove(worker_arr[0])
        return f'{worker_name} fired successfully'

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.__workers])

        if total_salaries > self.__budget:
            return 'You have no budget to pay your workers. They are unhappy'

        self.__budget -= total_salaries
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        total_expenses = sum([animal.money_for_care for animal in self.__animals])

        if total_expenses > self.__budget:
            return 'You have no budget to tend the animals. They are unhappy.'

        self.__budget -= total_expenses
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        return Zoo.__get_status(self.__animals, 'animals', Zoo.ANIMAL_TYPES_IN_ZOO)

    def workers_status(self):
        return Zoo.__get_status(self.__workers, 'workers', Zoo.WORKER_POSITIONS_IN_ZOO)

    @property
    def animals(self):
        return self.__animals

    @property
    def workers(self):
        return self.__workers

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name must be a string')

        self.__name = value

    @staticmethod
    def __get_status(target_attr, group_name: str, group_el_types):
        output = [f'You have {len(target_attr)} {group_name}']

        for name in group_el_types:
            elements = [repr(el) for el in target_attr if el.__class__.__name__ == name]
            output.append(f'----- {len(elements)} {name}s:')
            output.extend(elements)

        return '\n'.join(output)

    @staticmethod
    def __get_types(instances_arr):
        return {value.__class__.__name__ for value in instances_arr}

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

        if value < 0:
            raise ValueError('animal capacity must a positive number')

        return value

    @staticmethod
    def __worker_capacity_validator(value):
        if type(value) is not int:
            raise TypeError('worker capacity must be an integer number')

        if value < 0:
            raise ValueError('worker capacity must be a positive number')

        return value
