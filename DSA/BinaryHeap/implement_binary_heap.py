# Creation Of Binary Heap
class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.maxSize = size+1
        self.heapSize = 0

# Peak top of binary heap
def findPeak(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

# Extract Min / Max of binary heap
def findMin(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

def findMax(rootNode):
    if not rootNode:
        return
    return rootNode.customList[rootNode.heapSize]

# Traversal of binary heap
def traversal(rootNode):
    if not rootNode:
        return
    return [rootNode.customList[i] for i in range(1, rootNode.heapSize+1)]

# Size of binary heap
def findSize(rootNode):
    if not rootNode:
        return 0
    return rootNode.heapSize

# Reorder heap
def reOrderHeap(rootNode, heapIndex, heapType):

    if heapIndex == 1:
        return rootNode
    else:
        if heapType == 'Min':
            if rootNode.customList[heapIndex] < rootNode.customList[heapIndex//2]:
                temp = rootNode.customList[heapIndex]
                rootNode.customList[heapIndex] = rootNode.customList[heapIndex//2]
                rootNode.customList[heapIndex // 2] = temp
                reOrderHeap(rootNode, heapIndex // 2, heapType)
        else:
            if rootNode.customList[heapIndex] > rootNode.customList[heapIndex//2]:
                temp = rootNode.customList[heapIndex]
                rootNode.customList[heapIndex] = rootNode.customList[heapIndex//2]
                rootNode.customList[heapIndex // 2] = temp
                reOrderHeap(rootNode, heapIndex // 2, heapType)


# Insert value in binary heap
def insertNode(rootNode, value, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return 'Insert not allowed as heap is full!'
    else:
        rootNode.customList[rootNode.heapSize + 1] = value
        rootNode.heapSize += 1
        reOrderHeap(rootNode, rootNode.heapSize, heapType)
        return rootNode

def deleteNode(rootNode, value, heapType):
    if not rootNode:
        return 'Heap is empty.'
    elif value not in rootNode.customList:
        return 'Value does not exist in heap.'
    else:
        index_to_be_removed = rootNode.customList.index(value)
        if index_to_be_removed == rootNode.heapSize:
            rootNode.customList[index_to_be_removed] = None
        else:
            rootNode.customList[index_to_be_removed] = rootNode.customList[rootNode.heapSize]
            rootNode.customList[rootNode.heapSize] = None
            rootNode.heapSize -= 1
            if rootNode.heapSize - index_to_be_removed > 0:
                reOrderExtracedHeap(rootNode, index_to_be_removed, heapType)
        return rootNode



def reOrderExtracedHeap(rootNode, removedIndex, heapType):
    if removedIndex == rootNode.heapSize:
        return rootNode
    else:
        if removedIndex * 2 + 1 < rootNode.heapSize:
            leftChildIndex = removedIndex * 2
            rightChildIndex = removedIndex * 2 + 1
            if heapType == 'Min':
                if rootNode.customList[rightChildIndex]:
                    min_of_children = rootNode.customList.index(min(rootNode.customList[leftChildIndex], rootNode.customList[rightChildIndex]))
                else:
                    min_of_children = leftChildIndex

                if rootNode.customList[min_of_children] and rootNode.customList[removedIndex] >= rootNode.customList[min_of_children]:
                    temp = rootNode.customList[removedIndex]
                    rootNode.customList[removedIndex] = rootNode.customList[min_of_children]
                    rootNode.customList[min_of_children] = temp
                    reOrderExtracedHeap(rootNode, min_of_children, heapType)
            else:

                if rootNode.customList[rightChildIndex] is not None:
                    max_of_children = rootNode.customList.index(max(rootNode.customList[leftChildIndex], rootNode.customList[rightChildIndex]))
                else:
                    max_of_children = leftChildIndex

                if rootNode.customList[max_of_children] and rootNode.customList[removedIndex] < rootNode.customList[max_of_children]:
                    temp = rootNode.customList[removedIndex]
                    rootNode.customList[removedIndex] = rootNode.customList[max_of_children]
                    rootNode.customList[max_of_children] = temp
                    reOrderExtracedHeap(rootNode, max_of_children, heapType)











# Delete the node in binary heap

# Delete entire binary heap

# Test
newHeap = Heap(25)

newHeap = insertNode(newHeap, 10, 'Min')
newHeap = insertNode(newHeap, 20, 'Min')
newHeap = insertNode(newHeap, 30, 'Min')
newHeap = insertNode(newHeap, 40, 'Min')
newHeap = insertNode(newHeap, 50, 'Min')
newHeap = insertNode(newHeap, 60, 'Min')
newHeap = insertNode(newHeap, 70, 'Min')
newHeap = insertNode(newHeap, 80, 'Min')
newHeap = insertNode(newHeap, 90, 'Min')
newHeap = insertNode(newHeap, 100, 'Min')
newHeap = insertNode(newHeap, 110, 'Min')
newHeap = insertNode(newHeap, 5, 'Min')
newHeap = insertNode(newHeap, 20, 'Min')
newHeap = insertNode(newHeap, 10, 'Min')
newHeap = insertNode(newHeap, 10, 'Min')
newHeap = insertNode(newHeap, 3, 'Min')
newHeap = insertNode(newHeap, 10, 'Min')
print(traversal(newHeap))
# newHeap = deleteNode(newHeap, 20, 'Min')


# print(traversal(newHeap))
