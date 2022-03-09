from random import randint

class Queue:
    def __init__(self):
        self.values = []

    def __str__(self):
        return ' <- '.join([str(i) for i in self.values])

    def __len__(self):
        return len(self.values)

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        if len(self) > 0:
            self.values.pop(0)
        else:
            print('Queue is empty!')

    def peek(self):
        print(self.values[0])

    def delete(self):
        self.values = []
        return 'List is removed.'

q = Queue()
[q.enqueue(randint(1,20)) for _ in range(5)]
print(q)

q.dequeue()
q.peek()
print(q.delete())
print(q)