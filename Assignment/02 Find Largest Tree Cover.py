
def max_forest(forest_grid):

    visited = {}

    max_size = 0

    for r in range(0, len(forest_grid)):
        for c in range(0, len(forest_grid[0])):
            size = exploreSize(forest_grid, r, c, visited)
            if size > max_size:
                max_size = size

    return max_size


def exploreSize(forest_grid, r, c, visited):
    if not ((r >= 0) and (r < len(forest_grid))):
        return 0
    if not ((c >= 0) and (c < len(forest_grid[0]))):
        return 0

    # print(r,c)

    if forest_grid[r][c] == "W":
        return 0

    pos = str(r)+","+str(c)

    if pos in visited.keys():
        return 0

    visited[pos] = True

    size = 1

    size += exploreSize(forest_grid, r - 1, c, visited)
    size += exploreSize(forest_grid, r + 1, c, visited)
    size += exploreSize(forest_grid, r, c - 1, visited)
    size += exploreSize(forest_grid, r, c + 1, visited)

    return size


forest_grid = []

for i in range(int(input())):
    forest_grid.append(list(map(str, input().split(" "))))


#print(forest_grid)

value = max_forest(forest_grid)

if value > 0:
    print(value)
else:
    print(-1)

"""
5
T T T W W
T W W T T
T W W T T
T W T T T
W W T T T
"""
