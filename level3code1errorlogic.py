def solution(x, y):
    x = int(float(x))
    y = int(float(y))
    cycle = count = int(0)
    if x == 1 and y == 1:
        return '0'
    elif y == x + 1 or x == y + 1:
        return str(min(x, y))
    # elif max(x, y) % min(x, y) == 0:
    #     return 'impossible'
    else:
        while x != 1 or y != 1:
            if  x <= 0 or y <= 0:
                return 'impossible'
            cycle = int(max(x,y)/min(x,y))
            if min(x, y) == 1:
                count = count + max(x, y) - 1
                return str(count)
            elif x > y:
                x -= y * int(cycle)
            else:
                y -= x * int(cycle)
            count += cycle
        return str(count)


print(solution('9','6'))
print(solution('31','4'))
print(solution('2','1'))
print(solution('2','2'))
print(solution('1','1'))
print(solution('99999999999','1'))
print(solution('999999999999','999999999998'))
print(solution('9999999999999999','1'))
# print(solution(5,6))
# print(solution(7,4))
# print(solution(5,8))
# print(solution(5,4))
# print(solution(7,5))
# print(solution(30,29))