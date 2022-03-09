class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertSLL(self, value, loc):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if loc == 0:
                newNode.next = self.head
                self.head = newNode
            elif loc == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                node = self.head
                index = 0
                while index < loc - 1:
                    node = node.next
                    index += 1

                if self.tail is not node:
                    newNode.next = node.next
                    node.next = newNode
                else:
                    self.tail.next = newNode
                    self.tail = newNode

        return newNode

    def deleteSLL(self, loc):
        if self.head is None:
            return 'SLL is empty'

        if loc == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return 'Node removed from SLL!'
            else:
                tempNode = self.head.next
                self.head.next = None
                self.head = tempNode
                return 'Node removed from head!'

        elif loc == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return 'Node removed from SLL!'
            else:
                cNode = self.head
                while cNode.next.next is not None:
                    cNode = cNode.next

                cNode.next = None
                self.tail = cNode

        else:
            cNode = self.head
            index = 0
            while index < loc - 1:
                cNode = cNode.next
                index += 1

            if cNode.next is not self.tail:
                cNode.next = cNode.next.next
            else:
                cNode.next = self.tail.next
                self.tail = cNode

    def findLLength(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def findLLLengthRec(self, node):
        if self.head is None:
            return 'SLL is empty!'

        if node is None:
            return 0
        return 1 + self.findLLLengthRec(node.next)

    def searchVal(self, value):
        node = self.head
        while node is not None:
            if node.data == value:
                return value
            node = node.next
        return 'Value does not exist!'

    def searchValRec(self, node, value):
        if node.data == value:
            return node.data
        if node.next is not None:
            return self.searchValRec(node.next, value)
        else:
            return 'Value does not exist!'

    def findNthVal(self, index):
        node = self.head
        cIndex = 0
        while cIndex < index - 1:
            if node.next:
                node = node.next
            else:
                return 'Index value out of range!'
            cIndex += 1
        return node.data

    def findNFromEnd(self, index):
        resIndex = self.findLLLengthRec(self.head) - index
        return self.findNthVal(resIndex)

    def findMiddle(self):
        total_length = self.findLLength()
        middle = total_length // 2

        node = self.head
        index = 0
        while index < middle:
            node = node.next
            index += 1
        return node.data

    def findOccurrence(self, value):
        node = self.head
        count = 0
        while node is not None:
            if node.data == value:
                count += 1
            node = node.next
        return count

    def detectLoop(self):
        s = set()
        node = self.head
        while node is not None:
            if node not in s:
                s.add(node)
                node = node.next
            else:
                return 'Loop detected!'

        return 'No Loop!'

    def lengthOfLoop(self):
        d = {}
        node = self.head
        index = 0
        while node is not None:
            d[node] = index
            if node.next not in d:
                node = node.next
                index += 1
            else:
                return d[node] - d[node.next]
        return 'No loop detected!'

    def lengthOfLoopChase(self):
        slow = self.head
        fast = self.head
        count = 0
        while slow is not None:
            slow = slow.next
            if fast.next is None:
                return 'No Loop!'
            fast = fast.next.next
            count += 1
            if slow == fast:
                return count - 1

        return 'No Loop!'

    def reverseSLL(self):

        prev = None
        self.tail = self.head
        currNode = self.head

        while currNode is not None:
            next = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = next

        self.head = prev

    def checkPalindrome(self):
        count = 0
        # Find total length
        node = self.head
        while node is not None:
            node = node.next
            count += 1

        # Find middle
        if count % 2 == 0:
            mid = (count // 2) - 1
        else:
            mid = (count // 2)

        # Check palindrome
        loop_count = 0
        cNode = self.head
        while loop_count <= mid:
            last_ele = self.findNFromEnd(loop_count)
            if cNode.data != last_ele:
                return False
            cNode = cNode.next
            loop_count += 1

        return True

    def removeDuplicatesSorted(self):

        node = self.head
        same = self.head

        while node.next is not None:

            if node.next.data != same.data or node.next is None:
                same.next = node.next
                same = node.next

            node = node.next

        self.tail = same

    def removeDuplicatesUnsorted(self):

        node = self.head
        exists = set()
        exists.add(node.data)
        last_ele = self.head
        while node.next:

            if node.next.data not in exists:

                last_ele.next = node.next
                exists.add(node.next.data)
                last_ele = node.next

            if node.next == self.tail:
                last_ele.next = self.tail.next
                self.tail = last_ele

            if node.next:
                node = node.next


        self.tail = last_ele

    def swapNodes(self, nodeA_data, nodeB_data):
        nodeA_data = str(nodeA_data)
        nodeB_data = str(nodeB_data)
        nodeA_isHead = False
        nodeB_isHead = False
        nodeA_prev = None
        nodeB_prev = None
        if self.head.data == nodeA_data:
            nodeA_isHead = True
        if self.head.data == nodeB_data:
            nodeB_isHead = True

        node = self.head
        while node.next is not None:
            if node.next.data == nodeA_data and not nodeA_isHead:
                nodeA_prev = node
            if node.next.data == nodeB_data and not nodeB_isHead:
                nodeB_prev = node
            node = node.next


        if nodeA_isHead:
            nodeA_prev = self.head
            nodeA_next = nodeA_prev.next
            nodeA_prev.next = nodeB_prev.next.next
            nodeB_next = nodeB_prev.next
            nodeB_prev.next = nodeA_prev
            self.head = nodeB_next
            nodeB_next.next = nodeA_next

        if nodeB_isHead:
            nodeB_prev = self.head
            nodeB_next = nodeB_prev.next
            nodeB_prev.next = nodeA_prev.next.next
            nodeA_next = nodeA_prev.next
            nodeA_prev.next = nodeB_prev
            self.head = nodeA_next
            nodeA_next.next = nodeB_next


        if not nodeA_isHead and not nodeB_isHead:
            nodeA = nodeA_prev.next
            nodeB = nodeB_prev.next

            nodeA_next = nodeA.next
            nodeB_next = nodeB.next

            #Swap the next nodes first
            temp = nodeA_next
            nodeA.next = nodeB_next
            nodeB.next = temp

            # Swap the actual nodes now
            temp = nodeA_prev.next
            nodeA_prev.next = nodeB_prev.next
            nodeB_prev.next = temp

    def pairWiseSwap(self):
        index = 0
        node = self.head
        while node.next is not None:
            if index % 2 == 0:
                temp = node.data
                node.data = node.next.data
                node.next.data = temp
            index += 1
            node = node.next

    def moveLastToFirst(self):
        # Find the second last ele
        node = self.head
        while node.next.next:
            node = node.next

        node.next.next = self.head
        self.head = node.next
        node.next = None
        self.tail = node

    def evenAndOdd(self):
        node = self.head
        prev_node = None
        tail_node = self.tail
        while node.next != tail_node:
            if int(node.data) % 2 != 0:
                if self.head.data == node.data:
                    self.head = node.next
                    self.tail.next = node
                    next_node = node.next
                    node.next = None
                    self.tail = node
                    node = next_node
                else:
                    prev_node.next = node.next
                    self.tail.next = node
                    next_node = node.next
                    node.next = None
                    self.tail = node
                    node = next_node
            else:
                prev_node = node
                node = node.next

    def reverseLinkedList(self):
        node = self.head
        self.tail = self.head
        prev_node = None
        while node is not None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        self.head = prev_node

    def reverseSLLRecursion(self, currNode):
        if currNode.next is None:
            self.head = currNode
            return currNode
        else:
            tailNode = self.reverseSLLRecursion(currNode.next)
            currNode.next = None
            tailNode.next = currNode
            return currNode

    def reverseSLLTwoPointers(self):
        pass

def findIntersection(startNodeA, startNodeB):

    # Find length of both SLL
    a_length = 0
    nodeA = startNodeA
    while nodeA is not None:
        a_length += 1
        nodeA = nodeA.next

    b_length = 0
    nodeB = startNodeB
    while nodeB is not None:
        b_length += 1
        nodeB = nodeB.next

    # Find the difference in length
    diff_length = a_length - b_length if a_length >= b_length else b_length - a_length

    if diff_length > 0:
        if a_length > b_length:
            indexA = 0
            nodeA = startNodeA
            nodeB = startNodeB
            while indexA < diff_length:
                indexA += 1
                nodeA = nodeA.next
        else:
            indexB = 0
            nodeA = startNodeA
            nodeB = startNodeB
            while indexB < diff_length:
                indexB += 1
                nodeB = nodeB.next
    else:
        nodeA = startNodeA
        nodeB = startNodeB

    while nodeA != None and nodeB != None:
        if nodeA.data == nodeB.data:
            return 'Intersection at ' + nodeA.data

        nodeA = nodeA.next
        nodeB = nodeB.next

    return "No Intersection!"




P = SLinkedList()
P.insertSLL('11', -1)
P.insertSLL('13', -1)
P.insertSLL('21', -1)
P.insertSLL('32', -1)
P.insertSLL('23', -1)
P.insertSLL('44', -1)

S = SLinkedList()
P.insertSLL('22', -1)
P.insertSLL('33', -1)
P.insertSLL('23', -1)
P.insertSLL('44', -1)

print()

print(findIntersection(P.head, S.head))

node = P.head
while node:
    if node.next:
        print(node.data, end=' --> ')
    else:
        print(node.data, end=' ')
    node = node.next