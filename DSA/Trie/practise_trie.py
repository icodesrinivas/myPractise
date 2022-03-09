
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True

    def searchString(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node == None:
                return False
            current = node
        if current.endOfString == True:
            return True
        else:
            return False


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    deletable = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False

    deletable = deleteString(currentNode, word, index + 1)
    if deletable == True:
        root.children.pop(ch)
        return True
    else:
        return False



newTrie = Trie()
newTrie.insertString("Api")
newTrie.insertString("Apple")
print(newTrie.searchString('Api'))
deleteString(newTrie.root, 'Api', 0)
# newTrie.insertString("Appl")
print(newTrie.searchString('Api'))


p = {1:'A', 2:'B'}

print(p.get(1))