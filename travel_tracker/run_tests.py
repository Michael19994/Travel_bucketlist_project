import unittest

from models.countries import Country
from models.destinations import Destination
from models.destinations import Destination
from models.attractions import Attraction

class TestTravel(unittest.TestCase):
    def setUp(self):
        self.norway = Country("Norway", "Europe", 1)
        self.canada = Country("Canada", "North America", 2)
        self.tromso = Destination("Tromso", 1)
        self.whale_watching = Attraction("Whale Watching", "Orcas and Humpback Whales", 1, "20/12/2020", 2, True)

    def test_country_has_name(self):
        self.assertEqual("Norway", self.norway.name)

    def test_country_has_region(self):
        self.assertEqual("Europe", self.norway.region)

    def test_destination_has_name(self):
        self.assertEqual("Tromso", self.tromso.name)

    def test_destination_has_country(self):
        self.assertEqual(1, self.tromso.country)

    def test_attraction_has_name(self):
        self.assertEqual("Whale Watching", self.whale_watching.name)

    def test_attraction_has_description(self):
        self.assertEqual("Orcas and Humpback Whales", self.whale_watching.description)

    def test_attraction_has_destination_id(self):
        self.assertEqual(1, self.whale_watching.destination)

    def test_attraction_has_id(self):
        self.assertEqual(2, self.whale_watching.id)

    def test_attraction_has_date(self):
        self.assertEqual("20/12/2020", self.whale_watching.date)

    def test_attraction_has_visited(self):
        self.assertEqual(True, self.whale_watching.visited)

if __name__ == "__main__":
    unittest.main()

