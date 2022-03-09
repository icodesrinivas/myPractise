from random import randint
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        node = self.linkedList.head
        result = []
        if node == None:
            return 'Linked list is empty.'
        while node is not None:
            result.append(node.value)
            node = node.next
        return ' -> '.join(map(str, result))

    def push(self, value):
        node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = node
        else:
            node.next = self.linkedList.head
            self.linkedList.head = node

    def pop(self):
        if self.linkedList.head == None:
            print('List is empty')
        elif self.linkedList.head.next == None:
            self.linkedList.head = None
        else:
            self.linkedList.head = self.linkedList.head.next

    def peek(self):
        print(self.linkedList.head.value)

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def delete(self):
        self.linkedList.head = None
s = Stack()
s.push(65)
[s.push(randint(1,20)) for _ in range(5)]
s.push(333)
s.push(111)
print(s)
s.pop()
s.pop()

s.push(323)
print(s.linkedList.head.value)
s.peek()
print(s.isEmpty())
print(s)
s.delete()
print(s)
