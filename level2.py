
def solution(l):
    seperatedl = []
    integerl = []
    integera = []
    for el in l:
        seperatedl.append(el.split('.'))
    # print("seperatedl",seperatedl)
    for el in seperatedl:
        integerl.append(map(int, el))
    # print("integerl", integerl)
    for i, version in enumerate(integerl):
        integera.append(list(integerl[i]))
    # print("integera",integera)
    sortedlist = sorted(integera)
    # print("sortedIntList", sortedlist)
    sortedjoined = [('.'.join(str(e) for e in el)) for el in sortedlist]
    print("sortedjoined",sortedjoined)
    # print(sorted(l, key=None))

solution(["1.0.12", "1.0.2"])
# solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
# solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
# solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "01.0.20"])

