
def designerPdfViewer(h, word):
    print(ord('z') - 97)

    return max([h[ord(word[i]) - 97] for i in range(len(word))]) * len(word)


h = list(map(int, '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7'.split()))
print(designerPdfViewer(h, 'zaba'))