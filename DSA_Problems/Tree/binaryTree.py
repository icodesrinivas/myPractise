from DSA.Queue.implement_queue_linked_list import MyQueue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQ = MyQueue()
    customQ.enqueue(rootNode)
    while not(customQ.isEmpty()):
        root = customQ.dequeue()
        print(root.value.data)
        if root.value.leftChild:
            customQ.enqueue(root.value.leftChild)
        if root.value.rightChild:
            customQ.enqueue(root.value.rightChild)

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return "Success"
    customQ = MyQueue()
    customQ.enqueue(rootNode)
    while not(customQ.isEmpty()):
        root = customQ.dequeue()
        if root.value.leftChild is None:
            root.value.leftChild = newNode
            return "Success"
        else:
            customQ.enqueue(root.value.leftChild)

        if root.value.rightChild is None:
            root.value.rightChild = newNode
            return "Success"
        else:
            customQ.enqueue(root.value.rightChild)


drinks = TreeNode('Drinks')
hot = TreeNode('hot')
cold = TreeNode('cold')
drinks.leftChild = hot
drinks.rightChild = cold


newCola = TreeNode('Cola')
newFanta = TreeNode('Fanta')
newPepsi = TreeNode('Pepsi')
insertNodeBT(drinks, newCola)
insertNodeBT(drinks, newPepsi)
insertNodeBT(drinks, newFanta)

print()
print("Level Order Traversal")
levelOrderTraversal(drinks)

print()
# print(getDeepestNode(drinks).data)

print()
# dNode = getDeepestNode(drinks)
# deleteDeepestNode(drinks, dNode)
# levelOrderTraversal(drinks)

print()
print("Delete Node")
# deleteNode(drinks, drinks)
# levelOrderTraversal(drinks)