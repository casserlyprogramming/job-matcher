import unittest
from member import Member


class TestMember(unittest.TestCase):

    def test_jobs_for_developer(self):
        all_jobs = [
            {"title": "Software Developer", "location": "London"},
            {"title": "Marketing Internship", "location": "York"},
            {"title": "Data Scientist", "location": "London"},
            {"title": "Legal Internship", "location": "London"},
            {"title": "Project Manager", "location": "Manchester"},
            {"title": "Sales Internship", "location": "London"},
            {"title": "UX Designer", "location": "London"},
            {"title": "Software Developer", "location": "Edinburgh"},
        ]
        data = {
            "name": "Daisy",
            "bio": "I'm a software developer currently in Edinburgh but looking to relocate to London",
        }
        member = Member(data)
        member.assign_potential_jobs(all_jobs)
        self.assertListEqual(
            member.jobs, [{"title": "Software Developer", "location": "London"}]
        )
