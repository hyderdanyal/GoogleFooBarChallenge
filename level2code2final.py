def solution(l):
    l.sort(reverse=True)
    if sum(l) % 3 == 0:
        sol = ''.join(map(str, l))
        return int(sol)
    val = findpattern(l)
    if val and sum(val) % 3 == 0:
        sol = ''.join(map(str, val))
        return int(sol)
    else:
        return 0

def findpattern(arr):
    for i in range(len(arr)-1, -1, -1):
        temp = list(arr)
        temp.pop(i)
        if sum(temp) % 3 == 0:
            return temp
    for i in range(len(arr) - 1, -1, -1):
        temp2 = list(arr)
        temp2.pop(i)
        value = findpattern(temp2)
        if value:
            return value


print(solution([3, 1, 4, 1, 5, 9]))
print((solution([1, 2])))
print((solution([7,7,3])))
print((solution([7,7,7])))
print((solution([3, 1, 4, 1])))
print((solution([0, 0, 3])))
print((solution([0, 0, 1])))
print((solution([3,3,3])))
print((solution([7,7])))
