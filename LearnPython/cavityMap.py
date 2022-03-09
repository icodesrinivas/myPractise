def cavityMap(grid):

    if len(grid) > 2:
        x_list = []
        grid_list = [list(x) for x in grid]
        for depth_index in range(1, len(grid)-1):

            if len(grid[depth_index]) < 3:
                return grid

            for i in range(1, len(grid[depth_index]) - 1):
                left = grid[depth_index][i - 1]
                right = grid[depth_index][i + 1]
                top = grid[depth_index - 1][i]
                bottom = grid[depth_index + 1][i]
                sides = list(map(int, [left, right, top, bottom]))

                if all(list(map(lambda x: int(grid[depth_index][i]) > x, sides))):
                    x_list.append([depth_index, i])

        for item in x_list:
            grid_list[item[0]][item[1]] = 'X'

        grid = [''.join(x) for x in grid_list]

    return grid

cavityMap(['1112','1912','1892','1234'])

# s = 'sdad'
# print([list(k) for k in ['989','191','111']])
# print(s[1])