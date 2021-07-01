numbers = [1,1,1,1,1]
target = 3

from collections import deque

def solution(numbers, target):
    queue = deque()
    l = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-numbers[0],0])

    count = 0
    while queue:
        tmp_v, tmp_i = queue.popleft()
        tmp_i +=1
        if tmp_i < l:
            queue.append([tmp_v+numbers[tmp_i], tmp_i])
            queue.append([tmp_v-numbers[tmp_i], tmp_i])
        else :
            if tmp_v == target: count +=1

    return count

def solution2(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution2(numbers[1:], target-numbers[0]) + solution2(numbers[1:], target+numbers[0])

print(solution2(numbers,target))