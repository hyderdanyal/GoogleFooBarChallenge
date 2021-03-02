from collections import deque


def solution(map):
    height = len(map)
    width = len(map[0])
    row_num = [-1, 0, 0, 1]
    col_num = [0, -1, 1, 0]
    source = 0, 0, 1
    source_x, source_y, distance = source
    destination = height - 1, width - 1
    visited = [[{'visited': False, 'is1Visited': False} for i in range(width)] for j in range(height)]
    visited[source_x][source_y] = {'visited': True, 'is1Visited': False}
    # print(visited)
    q = deque()
    q.append((source_x,source_y, visited[source_x][source_y], distance))
    # print(q)
    while q:
        print(q)
        parent1Visited = parentVisited = False
        current = q.popleft()
        current_x, current_y, currentVisited, distance = current
        if currentVisited['is1Visited']:
            parent1Visited = True
        if currentVisited['visited']:
            parentVisited = True


        for i in range(4):
            row = current_x + row_num[i]
            column = current_y + col_num[i]

            if (0 <= column < width and 0 <= row < height)\
                    and ((map[row][column] == 0) or\
                         (not currentVisited['is1Visited'] and map[row][column] == 1)\
                                     or(currentVisited['visited'])):
                    # and (not currentVisited['visited']):
                if map[row][column] == 0:
                    if visited[row][column]['visited']:
                        continue
                    elif parent1Visited and not parentVisited:
                        visited[row][column]['is1Visited'] = True
                    else:
                        visited[row][column]['visited'] = True
                    if (row, column) == destination:
                        return distance + 1
                elif map[row][column] == 1 and not visited[row][column]['is1Visited']:
                    visited[row][column]['is1Visited'] = True
                adjacent_cell = (row, column, visited[row][column], distance+1)
                q.append(adjacent_cell)
                # is1Visited = False

                # if (adjacent_cell[0], adjacent_cell[1]) == destination:
                #     return distance+1








# print(solution([[0, 1, 0, 1, 0, 0, 0],
#                 [0, 0, 0, 1, 0, 1, 0]]))

#
# print(solution([[0,1,1],\
#                 [0,1,1],\
#                 [0,1,1],\
#                 [0,0,0]]))

# print(solution([[0,1], [1,0]]))
# print(solution([[0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))

# print(solution([[0, 0, 1, 0], \
#                 [0, 0, 0, 1],\
#                 [1, 1, 0, 0]]))
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
# print(solution([\
# [0, 1, 1, 0, 0],\
# [0, 1, 1, 1, 0],\
# [1, 0, 1, 1, 0],\
# [1, 0, 1, 1, 0],\
# [0, 0, 1, 1, 0],\
# [0, 1, 1, 1, 0],\
# [0, 1, 1, 1, 0],\
# [0, 0, 0, 0, 0]]))
#
# print(solution([\
# [0, 0, 1, 1, 0, 0, 0, 0],\
# [1, 0, 0, 0, 0, 1, 1, 0],\
# [0, 1, 1, 1, 1, 1, 1, 0],\
# [0, 1, 1, 1, 1, 1, 1, 0],\
# [0, 0, 0, 0, 0, 0, 0, 0]]))
#
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
