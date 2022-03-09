
class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        if self.head == None:
            return 'DLL is empty'
        else:
            node = self.head
            while node is not None:
                yield node
                node = node.next

    def createDoublyLinkedList(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    def insertDoublyLinkedList(self, value, location):
        newNode = Node(value)
        if location == 'start':
            if self.head == None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
        elif location == 'end':
            if self.head == None:
                self.head = newNode
                self.tail = newNode
            else:
                node = self.head
                while node.next is not None:
                    node = node.next
                node.next = newNode
                newNode.prev = node
                self.tail = newNode
        else:
            if location == 0:
                self.insertDoublyLinkedList(value, 'start')
            else:
                count = 0
                node = self.head
                while count < location - 1:
                    count += 1
                    node = node.next
                newNode.next = node.next
                newNode.prev = node
                node.next.prev = newNode
                node.next = newNode

    def traversal(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def reverseTraversal(self):
        node = self.tail
        while node is not None:
            print(node.value)
            node = node.prev

    def searchingDLL(self, value):
        node = self.head
        loc = 0
        while node is not None:
            if node.value == value:
                return f'The value {value} is located at position {loc}'
            loc += 1
            node = node.next
        return 'Value not found in DLL'

    def deleteDLL(self, location):
        if self.head == None:
            print('DLL is empty')
        else:
            if location == 'start':
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 'end':
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next.next is not None:
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                count = 0
                node = self.head
                if location == 0:
                    self.deleteDLL('start')
                else:
                    while count < location - 1:
                        count += 1
                        node = node.next
                    node.next.next.prev = node
                    node.next = node.next.next


d = DoublyLinkedList()
d.createDoublyLinkedList(1)
d.insertDoublyLinkedList(22, 'start')
d.insertDoublyLinkedList(32, 'start')
d.insertDoublyLinkedList(34, 'end')
d.insertDoublyLinkedList(366, 1)
d.insertDoublyLinkedList(121, 'end')
# d.traversal()
print([item.value for item in d])
# d.reverseTraversal()
# print(d.searchingDLL(1223))
# d.deleteDLL('start')
# d.deleteDLL('end')
# d.deleteDLL('end')
d.deleteDLL(3)
print([item.value for item in d])