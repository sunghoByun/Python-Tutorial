numbers = [3,30,343, 34,5,9]

strNumbers = [str(x) for x in numbers]

strNumbersList = [x*4 for x in strNumbers]

print(strNumbersList)
print([x[:4] for x in strNumbersList])
strNumbers.sort(key = lambda x : (x*4) [:4])
print(strNumbers)


def solution(numbers):
    answer = ""
    strNumber = [str(x) for x in numbers]
    strNumber.sort(key = lambda x : (x*4)[:4], reverse=True)
    if strNumber[0] == '0': return 0
    answer = ''.join(strNumber)

    return answer
