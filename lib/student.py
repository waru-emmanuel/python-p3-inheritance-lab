#!/usr/bin/env python

from user import User


knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


class Student(User):

    # must also have an attribute of learn

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def learn(self, new_information):
        self.knowledge.append(new_information)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    

   
        