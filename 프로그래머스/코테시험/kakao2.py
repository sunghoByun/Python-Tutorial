import math

n = 437674
k = 3


def is_prime_number(n):
    array = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                if i * j == n: return False
                array[i * j] = False
                j += 1

    return [i for i in range(2, n + 1) if array[i]]


def solution(n, k):
    p = 0

    def convert(n, k):
        T = "0123456789ABCDEF"
        q, r = divmod(n, k)
        if q == 0:
            return T[r]
        else:
            return convert(q, k) + T[r]

    def is_prime_number2(x):
        if x == 2 : return True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True


    pList = convert(n,k).split("0")
    pList2 = [int(i) for i in pList if i != '' and i != '1']

    answer = 0

    for num in pList2:
        if is_prime_number2(num):
            answer +=1

    return answer

print(solution(n,k))