import unittest
from city_function import region

class CityTest(unittest.TestCase):
    def test_city_country(self):
        city_country = region("Cairo","Egypt")
        self.assertEqual(city_country,"Cairo Egypt")

    def test_country_city_population(self):
        city_country_pop = region("cairo","Egypt",5000000)
        self.assertEqual(city_country_pop,"cairo Egypt 5000000")

unittest.main()
