from DSA.Queue.implement_queue_linked_list import MyQueue

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

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
    print(rootNode.data)
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
            print('My LC: ', root.value.leftChild.data)
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            print('My RC: ', root.value.rightChild.data)
            customQueue.enqueue(root.value.rightChild)

def insertNode(rootNode, value):
    if not rootNode:
        rootNode = BinarySearchTree(value)
    else:
        if value < rootNode.data:
            if rootNode.leftChild:
                rootNode.leftChild = insertNode(rootNode.leftChild, value)
            else:
                rootNode.leftChild = BinarySearchTree(value)
        else:
            if rootNode.rightChild:
                rootNode.rightChild = insertNode(rootNode.rightChild, value)
            else:
                rootNode.rightChild = BinarySearchTree(value)
    return rootNode



def searchValue(rootNode, value):
    if value == rootNode.data:
        return rootNode.data
    else:
        if value < rootNode.data:
            if not rootNode.leftChild:
                return 'Value not found!'
            else:
                return searchValue(rootNode.leftChild, value)
        else:
            if not rootNode.rightChild:
                return 'Value not found!'
            else:
                return searchValue(rootNode.rightChild, value)
    return 'Value not found!'

def findMinVal(rootNode):
    if not rootNode.leftChild:
        return rootNode
    while rootNode.leftChild:
        rootNode = rootNode.leftChild
    return rootNode

def deleteNode(rootNode, value):
    print(rootNode.data)
    if not rootNode:
        return rootNode
    else:
        if value < rootNode.data:
            if rootNode.leftChild:
                rootNode.leftChild = deleteNode(rootNode.leftChild, value)
            else:
                return 'The value does not exist!'
        elif value > rootNode.data:
            if rootNode.rightChild:
                rootNode.rightChild = deleteNode(rootNode.rightChild, value)
            else:
                return 'This value does not exist!'
        else:
            if rootNode.leftChild is None:
                temp = rootNode.rightChild
                rootNode = None
                return temp
            if rootNode.rightChild is None:
                temp = rootNode.leftChild
                rootNode = None
                return temp

            minValNode = findMinVal(rootNode.rightChild)
            print('minValNode', minValNode.data)
            rootNode.data = minValNode.data
            rootNode.rightChild = deleteNode(rootNode.rightChild, minValNode.data)

    return rootNode


BST = BinarySearchTree(10)
insertNode(BST, 20)
insertNode(BST, 15)
insertNode(BST, 25)
insertNode(BST, 5)
levelOrderTraversal(BST)
BST = deleteNode(BST, 10)
print('------')
levelOrderTraversal(BST)

