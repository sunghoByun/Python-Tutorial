#1이 될때까지

def whileNumber1(n : int, k : int) ->int:
    count = 0
    if n==1 : return 0

    while n!=1:
        if n%k ==0:
            count += 1
            n//=k
        else :
            count +=1
            n -=1

    return count

print(whileNumber1(17,3))

def whileNumber1LogN(n : int, k : int) -> int:
    count = 0

    while True:
        target = (n//k) * k
        count += (n-target)
        n = target
        if n<k:
            break

        count += 1
        n //= k

    count += (n-1)
    return count

print(whileNumber1LogN(17,3))

#곱하기 혹은 더하기

def mulOrAddMine(inputStr : str)-> int:
    result = 0

    for ch in inputStr:
        if ch=='0' or ch=='1' or result ==0:
            result += int(ch)
        else:
            result *= int(ch)

    return result

print(mulOrAddMine("567"))

#모험가 길드

def guildDefMine(N : int, inputStr : str) -> int:
    result = 0

    inputList = list(map(int,inputStr.split()))

    inputList.sort(reverse=True)

    while len(inputList) != 0 :
        k = inputList[0]
        for _ in range(k):
            inputList.pop(0)
            if len(inputList) == 0 : break

        result +=1

    return result

print(guildDefMine(5, "2 3 1 2 2"))

def guildDefAnswer(n : int, inputStr : str) -> int:
    data = list(map(int, inputStr.split()))
    data.sort()

    result = 0
    count = 0

    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0

    return result

print(guildDefAnswer(5, "2 3 1 2 2"))





