N = 5
lstTmp = [[55, 185],
[58, 183],
[88, 186],
[60, 175],
[46, 155]]

# N = int(input())
# lstTmp = []
# for _ in range(N):
#     lstTmp.append(list(map(int,input().split())))

lstAns = []

for i in range(len(lstTmp)):
    cnt = 1
    for j in range(len(lstTmp)):
        if i== j : continue
        else:
            if lstTmp[i][0] < lstTmp[j][0] and lstTmp[i][1] < lstTmp[j][1]:
                cnt +=1
    # lstAns += str(cnt) + " "
    lstAns.append(cnt)
# for i in range(len(listTmp)-1):
#     cnt = 1
#     for j in range(i+1, len(listTmp),1):
#         if listTmp[i][0] < listTmp[j][0] and listTmp[i][1] < listTmp[j][1]:
#             cnt +=1
#         # print(listTmp[i][0], listTmp[i][1])
#         # print(listTmp[j][0], listTmp[j][1])
#     lstAns.append(cnt)

print(lstAns, sep=' ')