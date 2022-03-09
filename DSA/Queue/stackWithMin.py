
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.min = []

    def __str__(self):
        node = self.head
        result = []
        while node is not None:
            result.append(str(node.value))
            node = node.next
        return ' -> '.join(result)

    def push(self, value):
        newNode = Node(value)
        if self.min:
            if value < self.min[-1]:
                self.min.append(value)
        else:
            self.min.append(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head == None:
            return 'Linked list is empty.'
        else:
            if self.head.next == None:
                self.head = None
                self.tail = None
                self.min = 0
            else:
                if self.head.value == self.min[-1]:
                    self.min.pop()
                self.head = self.head.next

    def findMin(self):
        if self.min:
            print(self.min[-1])
            return self.min[-1]
        else:
            print('Linked list is empty!')

s = LinkedList()

[s.push(i) for i in range(15,30,3)]

s.push(11)
s.push(8)
s.push(9)
s.pop()
s.pop()
s.pop()
s.findMin()
print(s)

