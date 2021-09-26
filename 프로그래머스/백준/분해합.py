N = int(input())
# listTmp = [0 for i in range(N+1)]
lstAns = []
for i in range(N+1):
    tmp = 0
    tmp += i
    for j in str(i):
        tmp += int(j)
    # listTmp[i] = tmp
    if tmp == N:
        lstAns.append(i)

if len(lstAns) == 0 : lstAns.append(0)

print(min(lstAns))