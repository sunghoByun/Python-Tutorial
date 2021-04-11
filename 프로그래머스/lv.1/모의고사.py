answers = [1,2,3,4,5]

supo1 = [1, 2, 3, 4, 5]
supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
ans = [0,0,0]
result =[]

def solution2(answers):
    for idx, answer in enumerate(answers):
        if supo1[idx % len(supo1)] == answer:
            ans[0] +=1
        if supo2[idx % len(supo2)] == answer:
            ans[1] +=1
        if supo3[idx % len(supo3)] == answer:
            ans[2] +=1

    for idx, value in enumerate(ans):
        if value == max(ans):
            result.append(idx+1)

    return result

def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    ans1,ans2,ans3 = 0,0,0

    for i in range(len(answers)):
        if supo1[i%len(supo1)] == answers[i]:
            ans1+=1
        if supo2[i%len(supo2)] == answers[i]:
            ans2+=1
        if supo3[i%len(supo3)] == answers[i]:
            ans3+=1

    max_key = max(ans1,ans2,ans3)
    keys = [ans1,ans2,ans3]
    max_keys=[]
    for i in range(len(keys)):
        if keys[i] == max_key:
            max_keys.append(i+1)

    return max_keys

print(solution(answers))

# 소스코드 - 자세한 사용법은 유튜브 영상을 참조하세요.
fruit = {'apple':5, 'grape':10, 'banana':7, 'peach':3, 'melon':2}

sorted1 = sorted(fruit.items(), key=lambda x:x[0])
sorted2 = sorted(fruit, key=lambda x:x[1])

print(sorted1)
print(sorted2)