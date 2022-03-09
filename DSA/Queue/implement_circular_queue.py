

class Queue:
    def __init__(self, maxSize):
        self.values = maxSize * [None]
        self.first = -1
        self.last = -1
        self.maxSize = maxSize

    def __str__(self):
        'a'.__len__()
        print('first', self.first)
        print('last', self.last)
        return ' <- '.join([str(i) for i in self.values])

    def __len__(self):
        count = 0
        for value in self.values:
            if value is not None:
                count += 1
        return count

    def enqueue(self, value):
        if len(self) == self.maxSize:
            print('Queue is full!')
            return 'Queue is full!'
        else:
            if self.last + 1 == self.maxSize and self.first != 0:
                self.last = 0
            else:
                if self.last == self.first and self.first == -1:
                    self.last += 1
                    self.first += 1
                else:
                    self.last += 1
            self.values[self.last] = value

    def dequeue(self):
        if len(self) == 0:
            print('Queue is empty')
            return 'Queue is empty'
        else:

            if self.first + 1 == self.maxSize:
                self.first = 0
            elif self.first == self.last:
                self.values = []
                self.first = -1
                self.last = -1
            else:
                self.first += 1
            self.values[self.first - 1] = None

    def peek(self):
        return self.values[self.first]
q = Queue(5)
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)
q.enqueue(6)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(22)
q.enqueue(12)
q.enqueue(14)
q.enqueue(144)
q.dequeue()
q.enqueue(44)
q.dequeue()
q.dequeue()
q.enqueue(124)
q.enqueue(4324)
q.enqueue(4324)
print(q.peek())
print(q)