def solution(l):
    seperatedl = [el.split('.') for el in l]
    # print("seperatedl",seperatedl)
    integerl = [map(int, el) for el in seperatedl]
    # print("integerl", integerl)
    # print(type(integerl))
    integera = [list(integerl[i]) for i, version in enumerate(integerl)]
    print("integera",integera)
    sortedlist = sorted(integera)
    # print("sortedIntList", sortedlist)
    sortedjoined = [('.'.join(str(e) for e in el)) for el in sortedlist]
    print("sortedjoined",sortedjoined)

# solution(["1.0.12", "1.0.2"])
solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
# solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
# solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "01.0.20"])