from DSA.Queue.implement_queue_linked_list import MyQueue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

bt = TreeNode('Drinks')
hot = TreeNode('Hot')
cold = TreeNode('Cold')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
fanta = TreeNode('Fanta')
cola = TreeNode('Cola')

bt.leftChild = hot
bt.rightChild = cold
hot.leftChild = tea
hot.rightChild = coffee
cold.leftChild = fanta
cold.rightChild = cola

def preOrderTraversal(rootNode):

    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
# print('preOrderTraversal')
# preOrderTraversal(bt)

def inOrderTraversal(rootNode):

    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    preOrderTraversal(rootNode.rightChild)
# print('inOrderTraversal')
# inOrderTraversal(bt)


def postOrderTraversal(rootNode):

    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
# print('postOrderTraversal')
# postOrderTraversal(bt)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    # Implement traversal with Queue with linked list
    # customQueue = MyQueue()
    # customQueue.enqueue(rootNode)
    # while not customQueue.isEmpty():
    #     root = customQueue.dequeue()
    #     print(root.value.data)
    #     if root.value.leftChild:
    #         customQueue.enqueue(root.value.leftChild)
    #
    #     if root.value.rightChild:
    #         customQueue.enqueue(root.value.rightChild)
    # Implement traversal with Queue with python list
    customList = []
    customList.append(rootNode)
    while len(customList) > 0:
        root = customList.pop(0)
        print(root.data)
        if root.leftChild:
            customList.append(root.leftChild)

        if root.rightChild:
            customList.append(root.rightChild)

print('levelOrderTraversal')
levelOrderTraversal(bt)


def searchValue(value, rootNode):
    if rootNode.data == value:
        return True
    customQueue = MyQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        if root.value.data == value:
            return True
        if root.value.leftChild:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQueue.enqueue(root.value.rightChild)
    return False
# print()
# print('searchValue')
# print(searchValue(value='Hota', rootNode=bt))

def insertNode(rootNode, value):
    newNode = TreeNode(value)

    customQueue = MyQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()

        if root.value.leftChild == None:
            root.value.leftChild = newNode
            return 'Node inserted'
        else:
            customQueue.enqueue(root.value.leftChild)

        if root.value.rightChild == None:
            root.value.rightChild = newNode
            return 'Node inserted'
        else:
            customQueue.enqueue(root.value.rightChild)

def getDeepetestNode(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = MyQueue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode):
    if rootNode is None:
        return
    deepestNode = getDeepetestNode(rootNode)
    customQueue = MyQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        if root.value.leftChild == deepestNode:
            root.value.leftChild = None
            return 'Deepest Node Removed!'
        else:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild == deepestNode:
            root.value.rightChild = None
            return 'Deepest Node Removed!'
        else:
            customQueue.enqueue(root.value.rightChild)


def deleteValue(rootNode, value):
    if rootNode is None:
        return
    else:
        customQueue = MyQueue()
        customQueue.enqueue(rootNode)
        deepestNode = getDeepetestNode(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == value:
                root.value.data = deepestNode.data
                deleteDeepestNode(rootNode)
                return "Deletion Success!"

            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)
        return 'Failed To Delete'
# print()
# print('getDeepestNode')
# print(getDeepetestNode(bt).data)
print(deleteValue(bt, 'Hot'))
print('levelOrderTraversal')
levelOrderTraversal(bt)
