

def solution(number, k):
    collectied = []

    for i, num in enumerate(number):
        while len(collectied) > 0 and collectied[-1] < num and k > 0:
            collectied.pop()
            k -= 1
        if k == 0 :
            collectied += number[i:]
            break
        collectied.append(num)

    if k > 0: collectied = collectied[:-k]

    return ''.join(collectied)

print(solution("4177252841",4))