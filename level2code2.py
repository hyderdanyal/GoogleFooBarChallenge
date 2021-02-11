def solution(l):
    index = len(l)
    notfound = True
    sortedarray = sorted(l, reverse=True)
    listsum = sum(l)
    remainder = listsum % 3
    if remainder == 0:
        print(f"completely divisible at length {len(l)} with sortedarray {sortedarray}")
    else:
        print(" not completely divisible at length", len(l))
        while notfound and index > 0:
            index -= 1
            innerfunction(sortedarray, notfound, index)


def innerfunction(sortedarray, notfound, index):
    popsortedarray = sortedarray.copy()
    popsortedarray.pop(index)
    print("index", index)
    # print("popsortedarray",popsortedarray)
    # print("sortedarray",sortedarray)
    listsum = sum(popsortedarray)
    remainder = listsum % 3
    if remainder == 0:
        print(f"completely divisible at length {len(popsortedarray)} with sortedarray {popsortedarray}")
        notfound = False
    else:
        print(f" not completely divisible at length {len(popsortedarray)} ")



solution([1, 4, 3, 1, 5, 9])
# solution([7,7,3])