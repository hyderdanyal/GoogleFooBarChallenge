def solution(x, y):
    x, y = long(x), long(y)
    count = 0

    while x != 1 or y != 1:
        if x <= 0 or y <= 0:
            return 'impossible'
        if y == 1:
            return str(count + x - 1)
        else:
            count += int(x/y)
            x, y = y, x % y
    return str(count)


print(solution('9','6'))
print(solution('31','4'))
print(solution('2','1'))
print(solution('1','2'))
print(solution('2','2'))
print(solution('1','1'))
print(solution('99999999999','1'))
print(solution('999999999999','999999999998'))
print(solution('9999999999999999','1'))