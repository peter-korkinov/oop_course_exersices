import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(4.0, 10.0)

    def test_instance_attr_are_set(self):
        self.assertEqual(4.0, self.vehicle.fuel)
        self.assertEqual(4.0, self.vehicle.capacity)
        self.assertEqual(10.0, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_method_works(self):
        self.vehicle.drive(2)
        expected_fuel_left = 4.0 - Vehicle.DEFAULT_FUEL_CONSUMPTION * 2
        self.assertEqual(expected_fuel_left, self.vehicle.fuel)

    def test_drive_method_raises_when_fuel_not_enough(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(3.21)
        self.assertEqual(4.0, self.vehicle.fuel)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_method_works(self):
        self.vehicle.fuel = 0.0
        self.vehicle.refuel(3.0)
        self.assertEqual(3.0, self.vehicle.fuel)

    def test_refuel_over_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(0.1)
        self.assertEqual(4.0, self.vehicle.fuel)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_str_magic_method(self):
        self.assertEqual(f'The vehicle has 10.0 horse power with 4.0 fuel left and'
                         f' {Vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption',
                         str(self.vehicle))


if __name__ == '__main__':
    unittest.main()
