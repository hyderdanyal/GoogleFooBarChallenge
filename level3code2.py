from collections import deque


def solution(map):
    height = len(map)
    width = len(map[0])
    # print(height, width)
    row_num = [-1, 0, 0, 1]
    col_num = [0, -1, 1, 0]
    source = 0, 0, False, 1
    source_x, source_y, _, _ = source
    destination = height - 1, width - 1
    # destination_x, destination_y = destination
    # distance = 1
    visited = [[{'visited':False, 'is1Visited':False} for i in range(width)] for j in range(height)]
    visited[source_x][source_y] = {'visited':True, 'is1Visited':False}
    # print(visited)
    q = deque()
    q.append(source)
    # print(q)
    while q:
        # print(q)
        current = q.popleft()
        current_x, current_y, is1Visited, distance = current


        for i in range(4):
            row = current_x + row_num[i]
            column = current_y + col_num[i]

            if (0 <= column < width and 0 <= row < height)\
                    and ((map[row][column] == 0 ) or\
                         (is1Visited == False and map[row][column] == 1))\
                    and (not visited[row][column]['visited']):
                visited[row][column]['visited'] = True
                if (map[row][column] == 1):
                    is1Visited = True
                adjacent_cell = (row, column, is1Visited, distance+1)
                q.append(adjacent_cell)
                is1Visited = False

            if (current[0], current[1]) == destination:
                return distance








print(solution([[0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0]]))

#
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
#
# # [0010]
# # [0001]
# # [1100]
#
# # [0, 1, 1, 0]
# # [0, 0, 0, 1]
# # [1, 1, 0, 0]
# # [1, 1, 1, 0]
# #
# # [0, 0, 0, 0, 0, 0]
# # [1, 1, 1, 1, 1, 0]
# # [0, 0, 0, 0, 0, 0]
# # [0, 1, 1, 1, 1, 1]
# # [0, 1, 1, 1, 1, 1]
# # [0, 0, 0, 0, 0, 0]
#
# # [0,1],
# # [1,0]
#
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

print(solution([[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[0, 0, 0, 0, 0, 0],\
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
