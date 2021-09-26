numbers = [3,30,34,5,9]

numbers = sorted(numbers, key = str, reverse= True)
firstNumbers = [str(i)[0] for i in numbers]
strTmp = ""
# while numbers:
#     number = numbers[0]
#     firstNumb = firstNumbers[0]
#
#     if firstNumb not in firstNumbers:
#         strTmp += str(number)
#     else:



x = "31"
y = "3"
z = "34"

tmpList = [x,y,z]
print(tmpList)
print(sorted(tmpList, key = lambda t : (t[0],t[1])))