
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age
        return self.age

    def find_age(self):
        return self.age

s = Student('Rahul', 15)
# print(getattr(s, 'set_age')(16))
print(getattr(s, 'find_age')())

