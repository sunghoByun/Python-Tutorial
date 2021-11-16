# priorities = [2,1,3,2]
# location = 2

priorities = [1,2,2,2]
location = 2

# priorities = [1]
# location = 0

def solution(priorities, location):
    answer = 0
    dicList = [[i,j] for i,j in enumerate(priorities)]

    while len(dicList) > 0:
        tmpNum = dicList[0]
        flg = False
        if len(dicList) == 1: return answer + 1 #마지막에 남은 경우 무한 루프에 돌게 됨
        for i, j in dicList[1:]:
            if tmpNum[1] < j:
                flg = False
                break
            flg = True

        if flg:
            dicList.pop(0)
            answer += 1
            if tmpNum[0] == location : break
        else: dicList.append(dicList.pop(0))

    return answer

print(solution(priorities,location))

def solution2(priorities, location):
    queue =  [[i,p] for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

print(solution2(priorities,location))
# def solution(priorities, location): #문제를 잘못이해함
#     mxTmp = max(priorities)
#     locList = [i for i in range(len(priorities))]
#     while True:
#         num = priorities[0]
#         loc = locList[0]
#
#         if num == mxTmp:
#             break
#         else:
#             priorities.append(priorities.pop(0))
#             locList.append(locList.pop(0))
#
#     answer = locList.index(location) + 1
#     print(priorities)
#     print(locList)
#     return answer

