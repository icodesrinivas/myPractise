
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.stacknum = None
        self.count = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack_list = LinkedList()

    def __str__(self):
        result = []
        node = self.stack_list.head
        while node is not None:
            result.append(str(node.value))
            node = node.next
        return ' <- '.join(result)

    def push(self, value):
        newNode = Node(value)
        if self.stack_list.head == None:
            newNode.stacknum = 0
            newNode.count = 1
            self.stack_list.head = newNode
        else:
            head_count = self.stack_list.head.count
            head_stacknum = self.stack_list.head.stacknum
            if head_count >= self.max_size:
                head_stacknum += 1
                head_count = 1
            else:
                head_count += 1

            newNode.stacknum = head_stacknum
            newNode.count = head_count
            newNode.next = self.stack_list.head
            self.stack_list.head = newNode

    def pop(self):
        if self.stack_list.head == None:
            return 'Stack is empty!'
        else:
            if self.stack_list.head.next == None:
                self.stack_list.head == None
            else:
                self.stack_list.head = self.stack_list.head.next

    def popAt(self, stacknum):
        node = self.stack_list.head
        if node.stacknum == stacknum:
            self.pop()
        else:
            while node.next is not None and node.next.stacknum != stacknum:
                node = node.next

            if node.next and node.next.stacknum == stacknum:
                node.next = node.next.next
            else:
                print(f'Stack {stacknum} is already empty')


s = Stack(3)
s.push(12)
s.push(15)
s.push(25)
s.push(33)
s.push(53)
s.push(123)
s.push(43)
s.push(73)
s.push(323)
s.push(233)


print(s)
s.popAt(3)
s.popAt(3)
print(s)