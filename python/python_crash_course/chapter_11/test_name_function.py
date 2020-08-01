import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py """

    def test_first_last_name(self):
        """ Do name like 'Janis Joplin' work? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ Do names like 'James Alfredo Noria' work? """
        formatted_name = get_formatted_name('james', 'noria', 'alfredo')
        self.assertEqual(formatted_name, 'James Alfredo Noria')

unittest.main()