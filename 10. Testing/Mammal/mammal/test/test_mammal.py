import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('dundi', 'pig', 'squeak')

    def test_instance_attr_are_set(self):
        self.assertEqual(self.mammal.name, 'dundi')
        self.assertEqual(self.mammal.type, 'pig')
        self.assertEqual(self.mammal.sound, 'squeak')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), 'dundi makes squeak')

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), self.mammal._Mammal__kingdom)

    def test_info(self):
        self.assertEqual(self.mammal.info(), 'dundi is of type pig')


if __name__ == '__main__':
    unittest.main()
