# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 3

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]

def solution(id_list, report, k):
    report = list(set(report))

    users = dict()
    reptUsers = dict()
    stopUsers = []

    for ids in id_list:
        users[ids] = []
        reptUsers[ids] = 0

    for rept in report:
        a,b = rept.split()
        users[a].append(b)
        reptUsers[b] +=1

    for key,value in reptUsers.items():
        if value >= k:
            stopUsers.append(key)
    answer = []
    for key, value in users.items():
        cnt = 0
        for v in value:
            if v in stopUsers:
                cnt +=1

        answer.append(cnt)

    return answer
# print(users)
# print(reptUsers)
# print(stopUsers)
# print(answer)