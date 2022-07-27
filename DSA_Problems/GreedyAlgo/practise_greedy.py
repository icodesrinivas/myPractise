
# import numpy as np
# def equalPairs(grid):
#     grid_T = np.array(grid).T
#     ans = 0
#     for row_ind in range(len(grid)):
#         for col_ind in range(len(grid_T)):
#             if grid[row_ind] == list(grid_T[col_ind]):
#                 ans += 1
#     return ans
#
#
# print(equalPairs([[3,1,2,2], [1,4,4,5], [2,4,2,2], [2,4,2,2]]))


class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[self.foods.index(food)] = newRating
        return self.ratings

foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]
f = FoodRatings(foods, cuisines, ratings)
print(f.changeRating("sushi", 99))
A = ['x','y','z']
B = [2,3,1]
C = [99,101,100]
print(list(sorted(zip(B,A,C))))
