nums = [1,2,7,6,4]

def isDecimal(a : int):
    bisDecimal = True
    tmp = a-1
    while(tmp>1):
        if a % tmp != 0 :
            tmp -=1
        else:
            bisDecimal = False
            return bisDecimal

    return bisDecimal

def solution(nums):
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if isDecimal(nums[i] + nums[j] + nums[k]) == True:
                    answer += 1

    return answer

#다른 사람의 풀이
# from itertools import combinations 라이브러리 기억하기
from itertools import combinations

def solution2(nums):
    answer = 0

    for a in combinations(nums,3):
        # a 는 tuple 형태, 리스트 내 원소 3개 조합 모두 탐색
        comb = sum(a)
        if isDecimal(comb) == True:
            answer += 1

    return answer

print(solution2(nums))