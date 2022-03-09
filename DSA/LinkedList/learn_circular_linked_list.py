
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCLinkedList(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = self.head

    def insertCLinkedList(self, value, location):
        if location == 'start':
            if self.head == None:
                node = Node(value)
                node.next = self.head
                self.head = node
                self.tail.next = node
            else:
                newNode = Node(value)
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
        elif location == 'end':
            if self.head == None:
                node = Node(value)
                self.head = node
                node.next = self.head
                self.tail = node
            else:
                node = self.head
                while node is not None:
                    if node.next == self.head:
                        break
                    node = node.next

                newNode = Node(value)
                node.next = newNode
                newNode.next = self.head
                self.tail = newNode
        else:
            count = 0
            node = self.head
            newNode = Node(value)
            if location == 0:
                self.insertCLinkedList(value, 'start')
            else:
                while count < location - 1:
                    node = node.next
                    count += 1

                newNode.next = node.next
                node.next = newNode

    def traversal(self):
        node = self.head
        if self.head == None:
            print('CSLL is empty')
        else:
            while node is not None:
                print(node.value)
                if node.next == self.head:
                    break
                node = node.next

    def searchCSLL(self, value):
        node = self.head
        if self.head == None:
            print('CSLL is empty')
        else:
            location = 0
            while node is not None:
                if node.next == self.head:
                    print('The value does not exist in CSLL')
                    break
                if node.value == value:
                    print(f'Value {value} exists in CSLL at location {location}')
                    break
                location += 1
                node = node.next

    def lenthCSLL(self):
        length = 0
        node = self.head
        while node is not None:
            if node.next == self.head:
                break
            length += 1
            node = node.next
        return length

    def deleteCSLL(self, location):

        if self.head == None or location > self.lenthCSLL():
            print('Either CSLL is empty or location out of index!')
        else:
            if location == 'start':
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 'end':
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next.next is not self.head:
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                count = 0
                node = self.head
                if location == 0:
                    self.deleteCSLL('start')
                else:
                    while count < location - 1:
                        count += 1
                        node = node.next

                    node.next = node.next.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail = self.head

s = CLinkedList()

s.createCLinkedList(1)
s.insertCLinkedList(22, 'end')
s.insertCLinkedList(83, 'end')
s.insertCLinkedList(11, 2)
s.insertCLinkedList(14, 3)
s.insertCLinkedList(12, 0)
s.insertCLinkedList(19, 'start')
s.insertCLinkedList(23, 0)
s.insertCLinkedList(133, 1)
print([item.value for item in s])
s.deleteCSLL(9)
# s.traversal()
# s.searchCSLL(233)
s.deleteEntireCSLL()
print([item.value for item in s])

