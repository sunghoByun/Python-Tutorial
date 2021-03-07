
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

#람다 표현식 연습

s = ['2 A', '1 B','4 C','1 A']
print("sorted s :",sorted(s))
print("s : ", s)
"""
두번째 문자순 정렬, 동일한 경우 앞 번호 순으로 정렬
"""

#람다식을 사용하지 않는 경우
def func(x):
    return x.split()[1], x.split()[0]


# new_s = s.sort(key=func)
# print("new_s : ", s.sort(key=func))

# new_s2 = s.sort(key = lambda x: (x.split()[1], x.split()[0]))
print("new_s2 : ", s.sort(key = lambda x: (x.split()[1], x.split()[0])))
print(s)
print()

def reorderLogFiles(logs: list):
    letters, digits = [], []

    for log in logs:
        print("log : ", log, ", log.split()[1] : ", log.split()[1])
        if log.split()[1].isdigit():
            digits.append(log)
            print("digits :", digits)
        else:
            letters.append(log)
            print("letters : ",letters)


    letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))
    print("letters :", letters)
    print("digits : ", digits)
    return letters + digits

print(reorderLogFiles(logs))