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

    def tend_animals(self):
        total_expenses = sum([animal.money_for_care for animal in self.__animals])

        if total_expenses > self.__budget:
            return 'You have no budget to tend the animals. They are unhappy.'

        self.__budget -= total_expenses
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = [f'You have {len(self.__animals)} animals']

        for ani_type in Zoo.ANIMAL_TYPES_IN_ZOO:
            anis_of_type = [repr(ani) for ani in self.__animals if ani.__class__.__name__ == ani_type]
            output.append(f'----- {len(anis_of_type)} {ani_type}s:')
            output.extend(anis_of_type)

        return '\n'.join(output)

    def workers_status(self):
        output = [f'You have {len(self.__workers)} workers']

        for position in Zoo.WORKER_POSITIONS_IN_ZOO:
            positions = [repr(worker) for worker in self.__workers if worker.__class__.__name__ == position]
            output.append(f'----- {len(positions)} {position}s:')
            output.extend(positions)

        return '\n'.join(output)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name must be a string')

        self.__name = value

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


from WildCatZoo.caretaker import Caretaker
from WildCatZoo.cheetah import Cheetah
from WildCatZoo.keeper import Keeper
from WildCatZoo.lion import Lion
from WildCatZoo.tiger import Tiger
from WildCatZoo.vet import Vet


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Firing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
