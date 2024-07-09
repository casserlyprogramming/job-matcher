import unittest
from location import LocationMatcher

class TestLocation(unittest.TestCase):

    def test_in_included(self):
        matcher = LocationMatcher("I'm looking for an internship in London")
        self.assertDictEqual(matcher.locations(), { "included": ["London"], "excluded": []})

    def test_in_excluded(self):
        matcher = LocationMatcher("I'm a software developer currently in Edinburgh but looking to relocate to London")
        self.assertDictEqual(
            matcher.locations(),
            { "included": ["London"], "excluded": ["Edinburgh"]}
        )

    def test_outside_of_excluded(self):
        matcher = LocationMatcher("I'm looking for a job in marketing outside of London")
        self.assertDictEqual(matcher.locations(), {"included": [], "excluded": ["London"]})

    def test_no_location(self):
        matcher = LocationMatcher("I'm looking for a design job")
        self.assertDictEqual(matcher.locations(), {"included": [], "excluded": []})
