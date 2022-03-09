from DSA.Queue.implement_queue_linked_list import MyQueue
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def levelOrderTraversal(self):
        if self == None:
            return
        customQueue = MyQueue()
        customQueue.enqueue(self)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild:
                print('leftChild', root.value.leftChild.data)
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                print('rightChild', root.value.rightChild.data)
                customQueue.enqueue(root.value.rightChild)

    def preOrderTravesal(self):
        if self == None:
            return
        print(self.data)
        if self.leftChild:
            self.leftChild.preOrderTravesal()
        if self.rightChild:
            self.rightChild.preOrderTravesal()

    def inOrderTraversal(self):
        if self == None:
            return
        if self.leftChild:
            self.leftChild.preOrderTravesal()
        print(self.data)
        if self.rightChild:
            self.rightChild.preOrderTravesal()

    def postOrderTraversal(self):
        if self == None:
            return
        if self.leftChild:
            self.leftChild.preOrderTravesal()
        if self.rightChild:
            self.rightChild.preOrderTravesal()
        print(self.data)

    def insertNode(self, value):
        newNode = BinarySearchTree(value)
        if self == None:
            self = newNode
        else:
            if value < self.data:
                if not self.leftChild:
                    self.leftChild = newNode
                else:
                    self.leftChild.insertNode(value)
            else:
                if not self.rightChild:
                    self.rightChild = newNode
                else:
                    self.rightChild.insertNode(value)
        return newNode

    def searchValue(self, value):
        if self == None:
            return 'BST is empty'
        if self.data == value:
            print('Value found')
            return self.data
        else:
            if value < self.data:
                if self.leftChild:
                    self.leftChild.searchValue(value)
                else:
                    print('Value not found in BST')
                    return 'Value not found in BST'
            else:
                if self.rightChild:
                    self.rightChild.searchValue(value)
                else:
                    print('Value not found in BST')
                    return 'Value not found in BST'

def findMinVal(rootNode):
    if rootNode is None:
        return rootNode
    while rootNode.leftChild:
        rootNode = rootNode.leftChild
    return rootNode

def deleteBSTNode(rootNode, value):
    if rootNode == None:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteBSTNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteBSTNode(rootNode.rightChild, value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        minVal = findMinVal(rootNode.rightChild)
        rootNode.data = minVal.data
        rootNode.rightChild = deleteBSTNode(rootNode.rightChild, minVal.data)

    return rootNode



def deleteBST(rootNode):
    rootNode.leftChild = None
    rootNode.rightChild = None
    rootNode = None
    return 'Success'

newBST = BinarySearchTree(70)
bt1 = newBST.insertNode(50)
# print('bt1.data',bt1.data)

bt2 = newBST.insertNode(90)
bt3 = newBST.insertNode(30)
bt4 = newBST.insertNode(60)
bt5 = newBST.insertNode(20)
bt6 = newBST.insertNode(40)
bt7 = newBST.insertNode(80)
bt8 = newBST.insertNode(100)
bt8 = newBST.insertNode(10)
bt8 = newBST.insertNode(110)
bt8 = newBST.insertNode(120)
bt8 = newBST.insertNode(75)
bt8 = newBST.insertNode(72)
bt8 = newBST.insertNode(55)
bt8 = newBST.insertNode(65)

# print(newBST)
deleteBSTNode(newBST, 50)
# print(findMinValue(newBST.rightChild))

# k = newBST.rightChild.findRightMinValue()
# print(minValueNode(newBST.rightChild).data)
newBST.levelOrderTraversal()

# print('preOrderTraversal')
# newBST.preOrderTravesal()

# newBST.searchValue(41)

# newBST.deleteValue(10)
# print(100)
# print()
# print('After delete!')
# newBST.levelOrderTraversal()

# anewBST = BinarySearchTree(10)
# anewBST.levelOrderTraversal()
# anewBST.deleteValue(10)
# anewBST.levelOrderTraversal()