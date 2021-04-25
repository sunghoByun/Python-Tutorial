d = [1,3,2,5,4]
budget = 9

def solution(d, budget):
    d.sort()
    answer = 0
    for a in d:
        if a <= budget:
            budget -= a
            answer +=1

    return answer



#다른 사람 풀이
def solution2(d, budget):
    d.sort()
    print(d)
    while budget < sum(d): #예산보다 합산이 큰 경우
        print(d.pop()) #큰 값부터 pop 시켜라
    return len(d)

print(solution2(d,budget))