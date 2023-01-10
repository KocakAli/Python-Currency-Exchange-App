from tabulate import tabulate

class User:
    def __init__(self,email,pw,name,surname,age):
        self.email = email
        self.password = pw
        self.name = name
        self.surname = surname
        self.age = age
