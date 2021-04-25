# def solution(n, lost, reserve):
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


for p, c in zip(sorted(participant),sorted(completion)):
    print(p,c)

    if p != c:
        print(p)

print(type(set(participant)))
print(set(participant))

import collections

A = collections.Counter(participant)
B = collections.Counter(completion)
print(type(A))
print(B)
print(A-B)
C = A-B

print(list(C.keys())[0])



