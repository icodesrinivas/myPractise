from DSA.Queue.implement_queue_linked_list import MyQueue
class AVLTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

    def searchValue(self, value):
        if self == None:
            return 'AVL Tree is empty'
        if self.data == value:
            print('Value found')
            return self.data
        else:
            if value < self.data:
                if self.leftChild:
                    self.leftChild.searchValue(value)
                else:
                    print('Value not found in AVL Tree')
                    return 'Value not found in AVL Tree'
            else:
                if self.rightChild:
                    self.rightChild.searchValue(value)
                else:
                    print('Value not found in AVL Tree')
                    return 'Value not found in AVL Tree'

