from jobs import Job

class Member:
    def __init__(self, initial_data):
        self.bio = initial_data["bio"].replace(",", "")
        self.name = initial_data["name"]
        self.jobs = []

    def assign_potential_jobs(self, all_jobs):
        for job in all_jobs:
            job_class = Job(job)
            if not job_class.search_location(self.bio):
                continue
            if job_class.search_title(self.bio):
                self.jobs.append(job)
