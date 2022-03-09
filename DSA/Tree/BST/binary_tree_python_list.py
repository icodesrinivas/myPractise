
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary Tree is Full!"
        else:
            self.customList[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1
            return "Node successfull inserted."

    def searchNode(self, value):
        if value in self.customList:
            return True
        else:
            return False

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            print(self.customList[index])
            self.preOrderTraversal(index*2)
            self.preOrderTraversal((index*2) + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            self.inOrderTraversal(index*2)
            print(self.customList[index])
            self.inOrderTraversal((index*2) + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            self.preOrderTraversal(index*2)
            self.preOrderTraversal((index*2) + 1)
            print(self.customList[index])

    def levelOrderTraversal(self, index):
        for item_index in range(index, self.lastUsedIndex):
            print(self.customList[item_index], end=" ")

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'Tree is empty'
        else:
            for i in range(1, self.lastUsedIndex):
                if self.customList[i] == value:
                    self.customList[i] = self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    return 'Node delete successfully!'
            return 'Value cannot be found!'

newBT = BinaryTree(8)
newBT.insertNode('Drinks')
newBT.insertNode('Hot')
newBT.insertNode('Cold')
newBT.insertNode('Coffee')
newBT.insertNode('Tea')
newBT.insertNode('Cola')
newBT.insertNode('Fanta')

print(newBT.customList)
# print(newBT.searchNode('Drinks'))
# print(newBT.preOrderTraversal(1))
print(newBT.deleteNode('Cold'))
print(newBT.customList)