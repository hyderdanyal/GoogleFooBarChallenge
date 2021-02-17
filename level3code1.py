def solution(m, f):
    cycle = 0
    if m == f:
        if m == 1 and f == 1:
            return str(0)
        return "impossible"
    if f == m + 1 or m == f + 1:
        return min(m, f)
    while m != 1 or f != 1:
        if m > f:
            m = m - f
            cycle = cycle + 1
        elif m < f:
            f = f - m
            cycle = cycle + 1
    return str(cycle)

# print(solution(2,1))
# print(solution(2,4))
# print(solution(4,7))
# print(solution(7,4))
# print(solution(5,8))
# print(solution(5,4))
# print(solution(7,5))
print(solution(30,29))


    # while cm != m or cf != f:
    #     if cm > m or cf > f:
    #         return "impossible"
    #     else:
    #         if cm + cf == m:
    #             cm = m
    #             cycle = cycle + 1
    #             if cm + cf == f:
    #                 cf = f
    #                 cycle = cycle + 1
    #                 return str(cycle)
    #             else:
    #                 pass
    #         elif cm + cf == f:
    #             cf = f
    #             cycle = cycle + 1
    #             if cm + cf == m:
    #                 cm = m
    #                 cycle = cycle + 1
    #                 return str(cycle)
    #             else:
    #                 pass
    #         elif m > f:
    #             cm = cm + cf
    #             cycle = cycle + 1
    #         elif f > m:
    #             cf = cm + cf
    #             cycle = cycle + 1
    #
    # return str(cycle)



    # while cm != m or cf != f:
    #     if cm > m or cf > f:
    #         return "impossible"
    #     elif m > f:
    #         if cm + cf == f :
    #             cf += cm
    #             cycle = cycle + 1
    #             if cm + cf == m:
    #                 cm = cm + cf
    #                 cycle = cycle + 1
    #         else:
    #             cm = cm + cf
    #             cycle = cycle + 1
    #     else:
    #         if cm + cf == m :
    #             cm += cf
    #             cycle = cycle +1
    #             if cm + cf == f:
    #                 cf = cm + cf
    #                 cycle = cycle + 1
    #         else:
    #             cf = cm + cf
    #             cycle = cycle + 1
    # return str(cycle)




# print(solution(2,1))
# print(solution(2,4))
# print(solution(4,7))
# print(solution(7,4))
# print(solution(5,8))
# print(solution(5,4))
# print(solution(7,5))
# print(solution(5,4))
