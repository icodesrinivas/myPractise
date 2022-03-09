
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class MyQueue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        result = []
        node = self.LinkedList.head
        while node is not None:
            result.append(str(node.value))
            node = node.next
        return ' -> '.join(result)

    def __len__(self):
        count = 0
        node = self.LinkedList.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            newNode.next = self.LinkedList.head
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode
        return newNode

    def dequeue(self):
        node = self.LinkedList.head
        if self.LinkedList.head == None:
            return 'Queue is empty!'
        else:
            if self.LinkedList.head.next == None:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
        return node

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

# q = MyQueue()
# [q.enqueue(i) for i in range(1,6)]
# print(q)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# print(q)
# [q.enqueue(i) for i in range(1,8)]
# q.dequeue()
# q.dequeue()
# print(q)
# print(q.LinkedList.head.value)
# print(q.LinkedList.tail.value)