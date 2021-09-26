import itertools

N,M = map(int, input().split())
listTmp = list(map(int, input().split()))

tmpMax = 0

for i in itertools.combinations(listTmp,3):
    tmp = sum(i)
    if tmp == M:
        tmpMax = tmp
        break
    else:
        if tmp < M and tmpMax < tmp:
            tmpMax = tmp

print(tmpMax)