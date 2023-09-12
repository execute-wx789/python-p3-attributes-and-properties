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
    def __init__(self,name="Example",job="ITC"):
        self.name = name.title() if type(name).__name__ == "str" and len(name) < 25 and len(name) > 1 else print("Name must be string between 1 and 25 characters.")
        self.job = job if APPROVED_JOBS.count(job) == 1 else print("Job must be in list of approved jobs.")