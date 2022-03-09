#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False


def deleteString(root, word, index):
    # Fetch the char from word based on index
    ch = word[index]
    print('ch', ch)
    # Check if the char exists in the root
    currentNode = root.children.get(ch)
    print('currentNode.endOfString',currentNode.endOfString)
    # Set the node as not to be deleted initially
    canThisNodeBeDeleted = False

    # If current node has 2 or more children, then simply move forward
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    # If we have reached the last node of the word to be deleted
    if index == len(word) - 1:
        # If last node children exists, then simply set end of string to false
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        # If last node children is empty, then remove the letter from root
        else:
            root.children.pop(ch)
            return True

    # If any other word is prefix of word to delete then move forward
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False

    # Check whether a particular char is deletable or not
    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
    # If the char is deletable, then pop the char from children, else return false
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("API")
newTrie.insertString("K")
newTrie.insertString("APPLE")
# print(newTrie.searchString("K"))
# deleteString(newTrie.root, "K", 0)
print(newTrie.root.children)
# print(newTrie.searchString("K"))