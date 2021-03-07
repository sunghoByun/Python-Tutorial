#방향 문제

def makeDirection():
    N = int(input())

    list_dir = input().split()

    dx = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
    dy = {'L': -1, 'R': 1, 'U': 0, 'D': 0}

    x,y = 1,1
    while len(list_dir) != 0 :
        dr = list_dir.pop(0)
        if x+dx[dr] > 0 and x + dx[dr]<N+1 and y+dy[dr] > 0 and y + dy[dr] < N+1:
            x += dx[dr]
            y += dy[dr]

    print(x,y)

#시간 문제

def countingTime():
    h = int(input())

    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j) + str(k):
                    count +=1

    print(count)

#왕실의 나이트 문제

def countingNight():
    position = input()
    x = ord(position[0]) - 96
    y = int(position[1])

    dx = [-1,1,-1,1,-2,-2,2,2]
    dy = [2,2,-2,-2,-1,1,-1,1]

    count = 0

    for i in range(len(dx)):
        if x + dx[i] > 0 and x + dx[i] < 9 and y + dy[i] > 0 and y + dy[i] < 9:
            count += 1

    print(count)

def sortingInputStr():
    inputStr = input()
    new_str = ""
    new_int = 0
    for ch in inputStr:
        if ch.isdigit():
            new_int += int(ch)
        else :
            new_str += ch

    print(''.join(sorted(new_str))+str(new_int))


