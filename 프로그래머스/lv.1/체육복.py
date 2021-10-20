# def solution(n, lost, reserve):
#     answer = 0
#     return answer


n = 10
losts = [1, 5, 8, 3, 7]
reserve = [7, 5, 2, 9, 6]


# aa = set(losts) - set(reserve)
# print(aa)

def solution(n, losts, reserve):
    setLosts = set(losts)
    setReserve = set(reserve)
    newLosts = setLosts - setReserve
    newReserve = setReserve - setLosts
    answer = n - len(losts) + len(setLosts & setReserve)

    for lost in newLosts:
        if lost - 1 in newReserve:
            answer += 1
            newReserve.remove(lost - 1)
        elif lost + 1 in newReserve:
            answer += 1
            newReserve.remove(lost + 1)

    return answer


# print(solution(n,losts,reserve))

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


def solution3(n, losts, reserve):
    stdList = [1] * (n + 2)
    anslist = []
    for lost in losts:
        stdList[lost] -= 1
    for res in reserve:
        stdList[res] += 1

    for i in range(1, n + 1, 1):
        if stdList[i] == 0:
            if stdList[i + 1] == 2:
                stdList[i + 1] -= 1
                stdList[i] += 1
            elif stdList[i - 1] == 2:
                stdList[i - 1] -= 1
                stdList[i + 1] += 1

    return len([x for x in stdList[1:-1] if x > 0])


print(solution3(n, losts, reserve))


def solution4(n, losts, reserve):
    losts = sorted(losts)
    answer = n - len(losts)
    for lost in losts:
        if lost in reserve:
            reserve.remove(lost)
            answer += 1
        elif lost + 1 in reserve:
            reserve.remove(lost + 1)
            answer += 1
        elif lost - 1 in reserve:
            reserve.remove(lost - 1)
            answer += 1
    return answer


print(solution4(n, losts, reserve))
