import collections

v = [[1, 4], [3, 4], [3, 10]]
def solution(v):
    xx = []
    yy = []
    for i in v:
        xx.append(i[0])
        yy.append(i[1])

    xxList = collections.Counter(xx)
    yyList = collections.Counter(yy)

    x2 = 0
    y2 = 0

    for x in xxList.items():
        if x[1] == 1:
            x2 = x[0]
    for y in yyList.items():
        if y[1] == 1:
            y2 = y[0]

    return [x2,y2]

print(solution(v))

