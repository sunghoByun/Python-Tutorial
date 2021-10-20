people = [90,70,50,80,50,10]
limit = 100
answer = len(people)
people2 = people
# for x in range(len(people)-1):
#
#     maxNum = 0
#     for y in people2:
#         if y <= limit - people[x] and limit - people[x] > maxNum:
#             maxNum = limit - y
#
#
#     if maxNum != 0:
#         people2.remove(y)
#         answer -= 1



print(answer)
