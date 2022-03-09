from random import randint
class Stack:
    def __init__(self):
        self.values = []

    def __str__(self):
        return ' -> '.join([str(item) for item in self.values])

    def __len__(self):
        return len(self.values)

    def add(self, value=None):
        self.values.append(value)
        print(self)

    def pop(self):
        self.values.pop()
        print(self)

    def isEmpty(self):
        return bool(self.values)

s = Stack()
[s.add(randint(1,20)) for _ in range(5)]
print(s)
s.pop()
s.pop()
s.add(23)
print(s.isEmpty())
print(len(s))