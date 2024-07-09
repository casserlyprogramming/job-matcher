import unittest
from jobs import Job

class TestJobs(unittest.TestCase):

    def test_successful_location_search(self):
        job = Job({"title": "UX Designer", "location": "London, UK"})
        self.assertTrue(job.search_location("I'm a designer from London UK"))

    def test_successful_title_search(self):
        job = Job({"title": "UX Designer", "location": "London, UK"})
        self.assertTrue(job.search_title("I'm a designer from London UK"))

    def test_false_location_search(self):
        job = Job({"title": "UX Designer", "location": "Edinburgh, UK"})
        self.assertFalse(job.search_location("I'm a designer from London UK"))

    def test_false_title_search(self):
        job = Job({"title": "Legal Internship", "location": "London"})
        self.assertFalse(job.search_title("I'm a designer from London UK"))

    def test_no_location_entered(self):
        job = Job({"title": "UX Designer", "location": "Edinburgh, UK"})
        self.assertTrue(job.search_location("I'm looking for a design job"))
