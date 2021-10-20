# m, n = map(int, input().split())
# lstTmp =[]
# for i in range(m):
#     strTmp = input()
#     lstTmp.append(strTmp)
# m = 8
# n = 8
# lstTmp = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBBBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
m = 10
n = 13
lstTmp =['BBBBBBBBWBWBW',
'BBBBBBBBBWBWB',
'BBBBBBBBWBWBW',
'BBBBBBBBBWBWB',
'BBBBBBBBWBWBW',
'BBBBBBBBBWBWB',
'BBBBBBBBWBWBW',
'BBBBBBBBBWBWB',
'WWWWWWWWWWBWB',
'WWWWWWWWWWBWB']


# strFirst = lstTmp[0][0]
# strSecond = ''
# if strFirst == 'W':
#     strSecond = 'B'
# else :
#     strSecond = 'W'

cnt = 0
strFirst ='B'
strSecond = 'W'

def countingChess(lstTmp):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if i%2 == 0 :
                if j%2 == 0 and lstTmp[i][j] == strSecond:
                        cnt +=1
                elif lstTmp[i][j] == strFirst:
                        cnt +=1
            else :
                if j % 2 == 0 and lstTmp[i][j] == strFirst:
                        cnt += 1
                elif lstTmp[i][j] == strSecond:
                        cnt += 1
    return cnt