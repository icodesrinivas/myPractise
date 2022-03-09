from DSA.Queue.implement_queue_linked_list import MyQueue
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    if rootNode.leftChild:
        preOrderTraversal(rootNode.leftChild)
    if rootNode.rightChild:
        preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    if rootNode.leftChild:
        inOrderTraversal(rootNode.leftChild)
    if rootNode.rightChild:
        inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    if rootNode.leftChild:
        postOrderTraversal(rootNode.leftChild)
    if rootNode.rightChild:
        postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue = MyQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild:
            print('LC: ', root.value.leftChild.data)
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            print('RC: ', root.value.rightChild.data)
            customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, value):
    if rootNode.data == value:
        return rootNode.data
    if value < rootNode.data:
        if rootNode.leftChild:
            searchNode(rootNode.leftChild, value)
        else:
            return 'Value does not exist!'
    else:
        if rootNode.rightChild:
            searchNode(rootNode.rightChild, value)
        else:
            return 'Value does not exist!'

def findMinValue(rootNode):
    if rootNode.leftChild is None:
        return rootNode
    while rootNode.leftChild:
        rootNode = rootNode.leftChild
    return rootNode

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, value):
    if not rootNode:
        return AVLNode(value)
    else:
        if value < rootNode.data:
            rootNode.leftChild = insertNode(rootNode.leftChild, value)
        else:
            rootNode.rightChild = insertNode(rootNode.rightChild, value)

        rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
        balance = getBalance(rootNode)

        if balance > 1 and value < rootNode.leftChild.data:
            return rightRotate(rootNode)
        if balance > 1 and value > rootNode.leftChild.data:
            leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)
        if balance < -1 and value > rootNode.rightChild.data:
            return leftRotate(rootNode)
        if balance < -1 and value < rootNode.rightChild.data:
            rightRotate(rootNode.rightChild)
            return leftRotate(rootNode)

        return rootNode

def deleteNode(rootNode, value):
    if not rootNode:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        minValNode = findMinValue(rootNode.rightChild)
        rootNode.data = minValNode.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, minValNode.data)

    balance = getBalance(rootNode)

    if balance > 1 and getBalance(rootNode.leftChild) > 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) < 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode





newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = deleteNode(newAVL, 20)
levelOrderTraversal(newAVL)
