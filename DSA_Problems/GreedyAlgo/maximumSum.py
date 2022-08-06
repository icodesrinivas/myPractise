"""
Maximum sum of increasing order elements from n arrays

Given n arrays of size m each. Find maximum sum obtained by selecting a number from each array such that the element selected from the i-th array is more than the element selected from (i-1)-th array. If maximum sum cannot be obtained then return 0.

â€‹Input : arr[ ] = {{1,7,4,3}, {4,2,5,1}, {9,5,1,8}}
Output : 18
Explanation:
We can select 4 from the first array,
5 from second array and 9 from the third array.
"""

def maximumSum(n, m, arr):

   total = max(arr[-1])
   n_max = total

   for i in range(n-2, -1, -1):
       arr[i].sort(reverse=True)
       found = False
       for j in arr[i]:
           if j < n_max:
               n_max = j
               total += n_max
               found = True
               break
       if not found: return 0

   return total


print(maximumSum(3, 4, [[1,7,4,3], [4,2,5,1], [9,5,1,8]]))