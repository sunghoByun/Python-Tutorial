people = [90,70,50,80,50,10]
limit = 100

def solution2(people, limit):
    answer = 0
    while people:
        person = people.pop(0)
        scdPerson = [i for i in people if i <= limit - person]
        if len(scdPerson) > 0 : people.remove(max(scdPerson))
        answer += 1
    return answer


def solution(people, limit):
    people.sort(reverse = True)
    i = 0
    j = len(people) -1
    answer = 0
    while i<= j:
        if people[i] + people[j] <= limit:
            i+= 1
            j-= 1
            answer +=1
        else:
            i+= 1
            answer += 1
    return answer

print(people)
# while i<= j :



