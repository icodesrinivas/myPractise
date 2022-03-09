# Check whether one list items are permutation of other list item

def permutation(arr1, arr2):
    return False if len(arr1) != len(arr2) else sorted(arr1) == sorted(arr2)


print(permutation('abcdf', 'fdcba'))
print(sorted('fdcba'))