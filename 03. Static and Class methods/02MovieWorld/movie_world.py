from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    _dvd_capacity = 15
    _customer_capacity = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        output = []
        output.extend([f'{repr(customer)}' for customer in self.customers])
        output.extend([f'{repr(dvd)}' for dvd in self.dvds])

        return '\n'.join(output)

    def add_customer(self, customer):
        if self.customer_capacity() > len(self.customers) and type(customer) is Customer:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.dvd_capacity() > len(self.dvds) and type(dvd) is DVD:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        dvd = self.get_dvd(dvd_id)
        customer = self.get_customer(customer_id)

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'

        if dvd.is_rented:
            return 'DVD is already rented'

        if dvd.age_restriction > customer.age:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        dvd = self.get_dvd(dvd_id)
        customer = self.get_customer(customer_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'

        return f'{customer.name} does not have that DVD'

    def get_customer(self, id):
        return [customer for customer in self.customers if customer.id == id][0]

    def get_dvd(self, id):
        return [dvd for dvd in self.dvds if dvd.id == id][0]

    @classmethod
    def dvd_capacity(cls):
        return cls._dvd_capacity

    @classmethod
    def customer_capacity(cls):
        return cls._customer_capacity


pesh = Customer('pesho', 18, 1)
print(pesh)
