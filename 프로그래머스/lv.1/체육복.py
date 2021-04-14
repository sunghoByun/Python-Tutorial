# def solution(n, lost, reserve):
#     answer = 0
#     return answer


n =5
losts = [1,2,3]
reserve = [2,3,4]

aa = set(losts) - set(reserve)
print(aa)

def solution(n, losts, reserve):
    setLosts = set(losts)
    setReserve = set(reserve)
    newLosts = setLosts - setReserve
    newReserve = setReserve - setLosts
    answer = n - len(losts) + len(setLosts & setReserve)

    for lost in newLosts:
        if lost-1 in newReserve:
            answer += 1
            newReserve.remove(lost-1)
        elif lost + 1 in newReserve:
            answer += 1
            newReserve.remove(lost + 1)

    return answer

print(solution(n,losts,reserve))

def solution2(n, lost, reserve):
    new_reserve = [r for r in reserve if r not in lost]
    new_lost = [l for l in lost if l not in reserve]
    # 진짜 없는 인원만 마지막에 빼기
    for r in new_reserve: 
        f = r - 1
        b = r + 1
        if f in new_lost:
            new_lost.remove(f) 
        elif b in new_lost:
            new_lost.remove(b)
    return n - len(new_lost)