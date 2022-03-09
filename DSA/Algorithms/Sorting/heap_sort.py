
def heapifyInsert(arr, index, heapType):

    rootIndex = index // 2
    if rootIndex >= 1:
        if arr[rootIndex] >= arr[index]:
            arr[rootIndex], arr[index] = arr[index], arr[rootIndex]
            heapifyInsert(arr, rootIndex, heapType)

    return arr

def insertHeap(arr, value):

    if len(arr) == 0:
        arr.insert(0, None)
        arr.append(value)
        return arr

    arr.append(value)
    arr = heapifyInsert(arr, len(arr)-1, 'Min')

    return arr

def heapifyExtract(arr):

    if len(arr) == 2:
        return arr

    else:
        i = 1
        while i < len(arr):
            leftChild = i * 2 if i * 2 < len(arr) else None
            rightChild = i * 2 + 1 if i * 2 + 1 < len(arr) else None
            if leftChild and rightChild:
                min_of_child = leftChild if min(arr[leftChild], arr[rightChild]) == arr[leftChild] else rightChild
            elif leftChild:
                min_of_child = leftChild
            else:
                min_of_child = rightChild

            if min_of_child:
                if arr[i] > arr[min_of_child]:
                    arr[i], arr[min_of_child] = arr[min_of_child], arr[i]
                    i = min_of_child
                else:
                    return arr
            else:
                i += 1
        return arr

def extractHeap(arr):

    if len(arr) == 2:
        arr.pop(1)
        return arr
    else:
        arr[1] = arr.pop()

    arr = heapifyExtract(arr)

    return arr


arr = [5, 9, 3, 1, 2, 8, 4, 7, 6]

def heap_sort(arr):

    heapify_arr = []

    for i in arr:
        insertHeap(heapify_arr, i)

    result = []
    while len(heapify_arr) > 1:
        result.append(heapify_arr[1])
        heapify_arr = extractHeap(heapify_arr)

    return result
arr = [5, 9, 3, 2, 8, 4, 7, 6]

# print(heap_sort(arr))


def heapify(customList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and customList[l] < customList[smallest]:
        smallest = l

    if r < n and customList[r] < customList[smallest]:
        smallest = r

    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)


def heapSort(customList):
    n = len(customList)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)

    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    # customList.reverse()
arr = [5, 9, 3, 2, 8, 4, 7, 6]
heapSort(arr)
print(arr)