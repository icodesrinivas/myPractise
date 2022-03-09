from random import randint
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class CDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        if self.head == None:
            return 'CDLL is empty'
        else:
            node = self.head
            while node is not None:
                yield node
                if node.next == self.tail.next:
                    break
                node = node.next

    def createCDLL(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.head.prev = node
            self.head.next = node
            self.tail = node
        else:
            return 'CDLL already exists!'

    def insertCDLL(self, value, location):
        newNode = Node(value)
        if location == 'start':
            if self.head == None:
                self.createCDLL(value)
            else:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
        elif location == 'end':
            if self.head == None:
                self.createCDLL(value)
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail.next:
                        break
                    node = node.next

                newNode.next = self.tail.next
                newNode.prev = node
                node.next = newNode
                self.tail = newNode
                self.head.prev = newNode
        else:
            count = 0
            node = self.head
            if location == 0:
                self.insertCDLL(value, 'start')
            else:
                while count < location - 1:
                    count += 1
                    node = node.next
                newNode.prev = node
                newNode.next = node.next
                node.next.prev = newNode
                node.next = newNode

    def reverseTraversal(self):
        node = self.tail
        while node.prev is not None:
            print(node.value)
            if node.prev == self.tail:
                break
            node = node.prev

    def deleteCDLL(self, location):
        if location == 'start':
            if self.head == None:
                return 'CDLL is empty'
            elif self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail.next = self.head.next
                self.head.next.prev = self.tail
                self.head = self.head.next
        elif location == 'end':
            if self.head == None:
                return 'CDLL is empty'
            elif self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail.prev.next = self.tail.next
                self.head.prev = self.tail.prev
                self.tail = self.tail.prev
        else:
            count = 0
            node = self.head
            if location == 0:
                self.deleteCDLL('start')
            else:
                while count < location - 1:
                    if node.next == self.head:
                        print('Location out of range.')
                        break
                    count += 1
                    node = node.next

                if self.tail == node.next:
                    self.tail = node
                node.next = node.next.next


        

cd = CDoublyLinkedList()
cd.createCDLL(1)
[cd.insertCDLL(randint(1, 100), 'start') for i in range(5)]
# cd.reverseTraversal()
print([item.value for item in cd])
cd.deleteCDLL(5)
print(cd.tail.value)
print([item.value for item in cd])