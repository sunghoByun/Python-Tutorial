numbers = [1,1,1,1,1]

def solutions(numbers):
    numbers.sort()

    sumNumbers=[]
    for a in range(len(numbers)):
        for b in range(a+1, len(numbers),1):
            sumNumbers.append(numbers[a]+numbers[b])

    sumNumbers= list(set(sumNumbers))
    if len(sumNumbers) >1 :
        sumNumbers.sort()
    return sumNumbers

print(solutions(numbers))