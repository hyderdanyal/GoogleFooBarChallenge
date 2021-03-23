# def solution(li):
#     divisibles = {}
#     possibilities = 0
#     for i in range(len(li)):
#         divisibles[li[i]] = []
#     for i in range(len(li)):
#         for j in range(i+1, len(li)):
#             if li[j] % li[i] == 0:
#                 # print(li[i], li[j])
#                 divisibleskey = li[i]
#                 divisiblesvalue = li[j]
#                 divisibles[divisibleskey].append(divisiblesvalue)
#             j += 1
#     print(divisibles)
#     for index in divisibles:
#         # print(divisibles[index])
#         # for val in divisibles[index]:
#             # print(val)
#             # print(len(divisibles[index]))
#         if len(divisibles[index]):
#             possibilities += len(divisibles[index])
#     possibilities -= len(divisibles[1])
#     # print(possibilities)
#     return possibilities
#         # if divisibles[el]:
#         #     print(len(divisibles[el]))

def solution(l):
    divisibles = [0] * len(l)
    # print(c)
    possibilities = 0

    for i in range(0, len(l)):
        j = 0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                divisibles[i] += 1
                possibilities += divisibles[j]
            # print(j)

    # print(c)
    return possibilities


print(solution([1, 1, 1]))
print(solution([1, 1, 2]))
print(solution([1, 2, 3, 4, 5, 6]))

