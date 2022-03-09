class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 'start':
                newNode.next = self.head
                self.head = newNode
            elif location == 'end':
                self.tail.next = newNode
                newNode.next = None
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    index += 1
                    tempNode = tempNode.next


                newNode.next = tempNode.next
                tempNode.next = newNode

    def traverseSLL(self):
        if self.head == None:
            print('SLL is empty')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def findValue(self, value):
        if self.head == None:
            print("Linked list is empty")
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == value:
                    return index
                index += 1
                node = node.next
            return "SLL does not contain value"

    def deleteValue(self, location):
        if self.head == None:
            print('Linked list is empty')
        else:
            if location in ['start',0]:
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
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
                index = 0
                node = self.head
                while index < location - 1:
                    index += 1
                    node = node.next

                node.next = node.next.next


    def findKthEleFromEnd(self, k):
        pointer1 = self.head
        pointer2 = self.head

        for i in range(k):
            pointer2 = pointer2.next

        while pointer2 is not None:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        return pointer1.value

    def partition(self, x):
        k = SLinkedList()
        node = self.head
        while node is not None:
            print(node.value)
            if k.head == None:
                newNode = Node(node.value)
                k.head = newNode
                k.tail = newNode
                newNode.next = None
            else:
                if node.value < x:
                    newNode = Node(node.value)
                    newNode.next = k.head
                    k.head = newNode
                else:
                    newNode = Node(node.value)
                    k.tail.next = newNode
                    k.tail = newNode
                print([node.value for node in k])
            node = node.next
        return k

    def sumNumbers(self, sll1, sll2):
        node1 = sll1.head
        node2 = sll2.head
        carry = 0
        result = Node(0)
        while node1 or node2:
            if node1 == None:
                node1 = Node(0)
            if node2 == None:
                node2 = Node(0)
            if carry + node1.value + node2.value > 9:
                result += str((carry + node1.value + node2.value) % 10)
                carry = (carry + node1.value + node2.value) // 10
                result += str(carry + node1.value + node2.value)
                carry = 0

            node1 = node1.next
            node2 = node2.next

        return int(result)
s = SLinkedList()

s.insertSLL(0,'start')
s.insertSLL(66,'end')
s.insertSLL(19,'end')
s.insertSLL(23,'end')
s.insertSLL(43,'end')
s.insertSLL(13,'end')
s.insertSLL(33,'end')

# print([node.value for node in s])
# s.deleteValue(8)
# print(s.findKthEleFromEnd(3))

# print([node.value for node in s.partition(20)])
# print([node.value for node in s])

j = SLinkedList()
j.insertSLL(7, 'start')
j.insertSLL(1, 'end')
print([node.value for node in j])
k = SLinkedList()
k.insertSLL(5, 'start')
k.insertSLL(1, 'end')
print([node.value for node in k])
print(s.sumNumbers(j, k))

# k = SLinkedList()
# k.traverseSLL()

