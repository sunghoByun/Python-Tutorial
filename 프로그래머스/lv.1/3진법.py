n = 125

def solution(n : int):
    tmp =""
    while n>0:
        tmp += str(n%3)
        n//=3

    print(tmp)

    answer = 0
    for i in range(len(tmp)-1 , -1 ,-1):
        answer += 3**(len(tmp)-i-1) * int(tmp[i])

    return answer

#다른 사람 풀이

def solution2(n : int):
    tmp = ""
    while n: #while n>0 과 동일
        tmp += str(n %3)
        n //= 3

    answer = int(tmp,3) #str 타입의 tmp를 3진법으로 판단하여 10진법으로 변환해줌



