from tabulate import tabulate

class User:
    def __init__(self,email,pw,name,surname,age):
        self.email = email
        self.password = pw
        self.name = name
        self.surname = surname
        self.age = age


    def show_personal_info(self):
        table = [
            ["Name", "Surname", "Age", "Email"],
            [self.name, self.surname, self.age, self.email]
        ]
        print(tabulate(table,headers="firstrow",tablefmt="fancy_grid"))