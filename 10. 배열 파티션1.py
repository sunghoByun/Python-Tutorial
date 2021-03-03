input = [1,4,3,2]

def sortNum(input : list) -> int:
    input.sort()
    sumNum = 0
    for i in range(0, len(input), 2):
        sumNum += min(input[i], input[i+1])

    return sumNum

# print(sortNum(input))

def pythonSortNum(input : list) -> int :
    print(sorted(input)[::2])
    return sum(sorted(input)[::2])

print(pythonSortNum(input))