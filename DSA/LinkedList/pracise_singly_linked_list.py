import copy
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = s.head
        while node is not None:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        if location == 'start':
            if self.head == None:
                self.head = Node(value)
                self.tail = self.head
            else:
                newNode = Node(value)
                newNode.next = self.head
                self.head = newNode
        elif location == 'end':
            if self.head == None:
                self.head = Node(value)
                self.tail = self.head
            else:
                node = self.head
                newNode = Node(value)
                while node is not None:
                    if node.next == None:
                        node.next = newNode
                        self.tail = newNode
                        break
                    else:
                        node = node.next
        else:
            index = 0
            node = self.head
            newNode = Node(value)
            if location - 1 < 0:
                newNode.next = node
                self.head = newNode
            else:
                while index < location - 1:
                    index += 1
                    node = node.next
                newNode.next = node.next
                node.next = newNode
                if newNode.next == None:
                    self.tail = newNode

    def traverse(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def searchSSL(self, value):
        node = self.head
        index = 0
        while node is not None:
            if node.value == value:
                print(f'The value {value} exists at the location {index} in the SLL')
                break
            index += 1
            node = node.next

    def deleteSSL(self, location):
        if self.head == None:
            print("SLL is empty")
        elif location == 'start':
            if self.head.next != None:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
        elif location == 'end':
            node = self.head
            if node.next == None:
                self.head = None
                self.tail = None
            else:
                while node.next.next is not None:
                    node = node.next
                node.next = None
                self.tail = node

        else:
            index = 0
            node = self.head
            if location - 1 < 0:
                self.head = self.head.next
            while index < location - 1:
                index += 1
                node = node.next
            node.next = node.next.next

    def deleteItem(self, node):
        temp = node
        node.value = node.next.value
        node.next = node.next.next

    def findNNodeSSL(self, location):
        node = self.head
        index = 0
        while index != location:
            index += 1
            node = node.next
        return node

    def recursiveSearchSSL(self, node, value):
        if node != None and node.value == value:
            return 0
        else:
            try:
                return 1 + self.recursiveSearchSSL(node.next, value)
            except:
                return f'Value {value} does not exist in SLL'

    def lenSLL(self):
        if self.head == None:
            return 0
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        print(count)
        return count

    def findNfromEndSSL(self, n):
        if self.head == None:
            return 'SLL is empty'
        else:
            pos = self.lenSLL() - n
            index = 0
            node = self.head
            while index < pos:
                node = node.next
                index += 1
            print(node.value)
            return node.value


    def findOccurenceSLL(self, value):
        count = 0
        node = self.head
        while node is not None:
            if node.value == value:
                count += 1
            node = node.next
        return count

    def detectLoopSLL(self):
        unique = set()
        node = self.head
        while node is not None:
            if node not in unique:
                unique.add(node)
            else:
                return 'Loop detected'
            node = node.next
        return 'No loop detected'

    def reverseSLL(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.tail = self.head
        self.head = prev

    def checkPalindrome(self):
        if self.head == None:
            return 'SLL is empty'
        if self.head.next == None:
            return True
        node = self.head
        result = []
        while node is not None:
            result.append(node)
            node = node.next

        node = self.head
        while node is not None:
            i = result.pop()
            if i.value != node.value:
                return False
            node = node.next
        return True

    def removeSortedDuplicates(self):
        current = self.head.next
        prev = self.head
        while current is not None:
            if current.value == prev.value:
                prev.next = current.next
            else:
                prev = current
            current = current.next

    def removeUnsortedDuplicates(self):
        output = []
        prev = None
        curr = self.head
        while curr is not None:
            if curr.value not in output:
                output.append(curr.value)
                prev = curr
            else:
                prev.next = curr.next
                prev = curr
            curr = curr.next

    def swapPairs(self):
        count = 0
        curr = self.head
        prev = None
        while curr is not None:
            if count % 2 == 1 and prev:
                temp = prev.value
                prev.value = curr.value
                curr.value = temp
                prev = curr
                count += 1
            else:
                prev = curr
                count += 1

            curr = curr.next

    def swapTailToHead(self):
        curr = self.head
        prev = None
        while curr.next is not None:
            prev = curr
            curr = curr.next

        lastNode = prev.next
        prev.next = None
        self.tail = prev
        lastNode.next = self.head
        self.head = lastNode

    def intersectionSLL(self, head):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        intersection = []
        item = head
        while item is not None:
            if item.value in result:
                intersection.append(item.value)
            item = item.next

        return intersection



s = SinglyLinkedList()


[s.insertSLL(i, 'end') for i in [11, 11, 13, 22, 151, 1415,1661, 2997]]



# s.traverse()
# s.searchSSL(22)

# print([node.value for node in s])
# k = s.findNNodeSSL(5)

# print(s.findOccurenceSLL(11))
# print(s.detectLoopSLL())
# print([node.value for node in s])
# s.removeUnsortedDuplicates()
print([node.value for node in s])
# s.swapPairs()
s.swapTailToHead()
k = SinglyLinkedList()
[k.insertSLL(i, 'end') for i in [99, 13, 22, 151, 1661, 2997, 431]]
print([node.value for node in k])
print('intersection', s.intersectionSLL(k.head))
# print([node.value for node in s])
# print(s.checkPalindrome())