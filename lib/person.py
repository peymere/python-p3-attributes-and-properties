#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self.name = name 
        self.job = job

    def get_name(self):
        print("Retrieving name")
        print(self._name)
        return self._name

    def set_name(self, name):
        if (type(name) == (str)) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}")
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        print("Retrieving job")
        print(self._job)
        return self._job

    def set_job(self, job):
        if (type(job) == (str)) and job in APPROVED_JOBS:
            print(f"Setting job to {job}")
            self._job = job.title()
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)


peyton = Person("peyton meredith", "Teacher")
peyton.name
peyton.job = "Marketing"
