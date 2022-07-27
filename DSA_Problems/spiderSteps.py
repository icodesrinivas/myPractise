
"""
The Spider Steps
A spider present at the bottom of the well of height H, needs to get out of it. The walls of the well are very slippery. In each step, it climbs U metres and slips down D metres. If in the last step, the spider gets out of the well by climbing U metres, it does not slip back. Find the number of steps the spider takes.
Input:
H = 200, U = 50, D = 1
Output: 5
Explaination:
First Step: 50 -1 = 49
Second Step: 49 + 50 - 1 = 98
Third Step: 98 + 50 - 1 = 147
Fouth Step: 147 + 50 - 1 = 196
Fifth Step: Reach beyond H.
"""
from math import ceil
def minStep(H, U, D):

    if U > H:
        return 1

    if (H-U) // (U-D) <= H-U:
        return (H-U) // (U-D) + 2
    else:
        return (H-U) // (U-D) + 1

print(minStep(10, 4, 1))