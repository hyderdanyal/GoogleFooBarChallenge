def solution(map):
    height = len(map)
    width = len(map[0])
    source_path = shortest_path(0, 0, map)
    # print(source_path)
    destination_path = shortest_path(height - 1, width - 1, map)
    # print(destination_path)
    # visited = []

    # ans = 2 ** 32 - 1
    ans = 401
    for i in range(height):
        for j in range(width):
            if source_path[i][j] and destination_path[i][j]:
                ans = min(source_path[i][j] + destination_path[i][j] - 1, ans)
    return ans


def shortest_path(x, y, map):
    height = len(map)
    width = len(map[0])
    row_num = [-1, 0, 0, 1]
    col_num = [0, -1, 1, 0]
    visited = [[None for i in range(width)] for i in range(height)]
    visited[x][y] = 1
    # print(visited)

    arr = [(x, y)]
    while arr:
        current_x, current_y = arr.pop(0)
        # for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        #     print(i)
        for i in range(4):
            # nx, ny = x + i[0], y + i[1]
            row = current_x + row_num[i]
            column = current_y + col_num[i]
            if 0 <= row < height and 0 <= column < width:
                if visited[row][column] is None:
                    visited[row][column] = visited[current_x][current_y] + 1
                    if map[row][column] == 1:
                        continue
                    arr.append((row, column))

    return visited


# map = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] #solution 21
# map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] #solution 7
# map = [[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]] #solution 7
# map = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] #solution 7
# map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0]]  # solution 11

# print(solution(map))

print(solution([[0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0]]))

print(solution([[0,1,1],\
                [0,1,1],\
                [0,1,1],\
                [0,0,0]]))

print(solution([[0,1], [1,0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))

print(solution([[0, 0, 1, 0], \
                [0, 0, 0, 1],\
                [1, 1, 0, 0]]))

print(solution([\
[0, 1, 1, 0, 0],\
[0, 1, 1, 1, 0],\
[1, 0, 1, 1, 0],\
[1, 0, 1, 1, 0],\
[0, 0, 1, 1, 0],\
[0, 1, 1, 1, 0],\
[0, 1, 1, 1, 0],\
[0, 0, 0, 0, 0]]))

print(solution([\
[0, 0, 1, 1, 0, 0, 0, 0],\
[1, 0, 0, 0, 0, 1, 1, 0],\
[0, 1, 1, 1, 1, 1, 1, 0],\
[0, 1, 1, 1, 1, 1, 1, 0],\
[0, 0, 0, 0, 0, 0, 0, 0]]))

print(solution([
[0, 0, 0, 0, 0, 0],\
[1, 1, 1, 1, 1, 0],\
[0, 0, 0, 0, 0, 0],\
[0, 1, 1, 1, 1, 1],\
[0, 1, 1, 1, 1, 1],\
[0, 0, 0, 0, 0, 0],\
[0, 0, 0, 0, 0, 0],\
[1, 1, 1, 1, 1, 0],\
[0, 0, 0, 0, 0, 0],\
[0, 1, 1, 1, 1, 1],\
[0, 1, 1, 1, 1, 1],\
[0, 0, 0, 0, 0, 0],\
[0, 0, 0, 0, 0, 0],\
[1, 1, 1, 1, 1, 0],\
[0, 0, 0, 0, 0, 0],\
[0, 1, 1, 1, 1, 1],\
[0, 1, 1, 1, 1, 1],\
[0, 0, 0, 0, 0, 0],\
[0, 0, 0, 0, 0, 0],\
[1, 1, 1, 1, 1, 0],\
[0, 0, 0, 0, 0, 0],\
[0, 1, 1, 1, 1, 1],\
[0, 1, 1, 1, 1, 1],\
[0, 0, 0, 0, 0, 0]]))

