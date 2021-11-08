

def solution(number, k):
    collectied = []

    for i, num in enumerate(number):
        while len(collectied) > 0 and collectied[-1] < num and k > 0:
            #collected 리스트가 1개 이상 있으면서, 가장 최근 숫자가 비교하는 숫자보다 작고, 뽑아야 되는 숫자가 0 이상이면
            collectied.pop()
            #안에 있는걸 한개 씩 뺀다
            k -= 1
            #뽑아야 되는 갯수 한개 씩 감소
        if k == 0 : #이미 다 뽑았다면, 뒤에 있는 나머지 수를 합친다
            collectied += number[i:]
            break
        collectied.append(num)

    if k > 0: collectied = collectied[:-k]

    return ''.join(collectied)

number = "999"
k = 2


def solution2(number, k):
    collect = []
    for i, num in enumerate(number):
        while len(collect) > 0 and collect[-1] < num and k > 0:
            collect.pop()
            k -= 1
        if k == 0:
            collect += number[i:]
            break
        collect.append(num)

    if k > 0: collect = number[:-k]

    return ''.join(collect)

print(solution2(number,k))