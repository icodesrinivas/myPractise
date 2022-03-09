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

    def getIntersectionNode(self, headB):

        listA = []
        nodeA = self.head
        while nodeA is not None:
            listA.append(nodeA.value)
            nodeA = nodeA.next

        nodeB = headB
        while nodeB is not None:
            print(nodeB.value)
            if nodeB.value in listA:
                print(f'Intersected at \'{nodeB.value}\'')
                break
            else:
                nodeB = nodeB.next
        print('No intersection')





s = SLinkedList()
[s.insertSLL(_, 'end') for _ in [4,1,8,4,5]]
k = SLinkedList()
[k.insertSLL(_, 'end') for _ in [5,6,1,8,4,5]]
[4,1,8,4,5]
[5,6,1,8,4,5]

print([i.value for i in s])
print([j.value for j in k])

s.getIntersectionNode(k.head)