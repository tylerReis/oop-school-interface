class Person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = int(age) ## todo handle casting error if age valid
        self.role = role