import unittest
from city_functions import some_place


class NameCityCountry(unittest.TestCase):

    def test_city_country(self):
        """ Do we receive 'Lima, Peru' as output """
        nice_name = some_place('lima', 'peru')
        self.assertEqual(nice_name, 'Lima, Peru')

    def test_population(self):
        """ Do we receive population as output? """
        nice_name = some_place('lima', 'peru', 1000000)
        self.assertEqual(nice_name, 'Lima, Peru - population 1000000')

unittest.main()
