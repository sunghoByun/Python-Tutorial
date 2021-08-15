import collections

s = "asda"


coCounter = collections.Counter(s.lower())
a = []


maxV = coCounter.most_common(1)[0][1]

for k, v in coCounter.items():
    if v == maxV:
        a.append(k)

print(a)

a.sort()
#
if "s" in a:
    i = a.index('s')
    del a[i]
    a.insert(0,'SS')


if "o" in a:
    i = a.index('o')
    del a[i]
    a.insert(0,'O')

if "t" in a:
    i = a.index('t')
    del a[i]
    a.insert(0,'T')

answer = ''.join(a)
print(answer)

def solution(s):
    answer = ''
    coCounter = collections.Counter(s.lower())
    a = []

    maxV = coCounter.most_common(1)[0][1]

    for k, v in coCounter.items():
        if v == maxV:
            a.append(k)

    a.sort()

    if "s" in a:
        i = a.index('s')
        del a[i]
        a.insert(0, 'SS')

    if "o" in a:
        i = a.index('o')
        del a[i]
        a.insert(0, 'O')

    if "t" in a:
        i = a.index('t')
        del a[i]
        a.insert(0, 'T')

    answer = ''.join(a)
    return answer