import unittest
from city_country import get_city_country


class NamesTestCase(unittest.TestCase):

    def test_get_city_country(self):
        sentence = get_city_country('Beijing', 'China')
        self.assertEqual(sentence, 'Beijing,China')

    def test_get_city_country_population(self):
        sentence = get_city_country('Beijing', 'China', 22000000)
        self.assertEqual(sentence, 'Beijing,China-population: 22000000')


if __name__ == '__main__':
    unittest.main()
