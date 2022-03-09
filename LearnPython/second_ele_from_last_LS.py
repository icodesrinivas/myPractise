class LinkedList:

    def __init__(self, data):
        self.node = data
        self.next = None

    def getLen(self):
        current_node = self
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def removeNode(self):

        current_node = self

        if current_node.next.next != None:
            self.next = current_node.next.next
        else:
            self.next = None


        self.node = self.next.node

a = LinkedList("A")
b = LinkedList("B")
c = LinkedList("C")
d = LinkedList("D")

a.next = b
b.next = c
c.next = d

op = a.getLen()
print(op)
c.removeNode()
op = a.getLen()
print(op)
