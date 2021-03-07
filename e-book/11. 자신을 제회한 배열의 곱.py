input = [3,4,5,6]

def mulExceptSelf(input : list) -> list:
    returnList =[]
    mulNum = 1
    for num in input:
        mulNum *= num

    for num in input:
        returnList.append(mulNum//num)

    return returnList

print(mulExceptSelf(input))

def usingTwoList(input : list):
    left, right=[], []
    returnList = []

    p = 1
    for i in range(len(input)):
        left.append(p)
        p *= input[i]

    p=1
    for j in range(len(input)-1, -1, -1):
        right.append(p)
        p *= input[j]

    right.reverse()

    for k in range(len(input)):
        returnList.append(left[k] * right[k])

    return returnList


print(usingTwoList(input))