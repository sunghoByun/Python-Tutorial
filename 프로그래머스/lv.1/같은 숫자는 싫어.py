arr =[1,1,3,3,0,1,1]

n_arr = [arr[0]]

for i in range(1,len(arr)):
    if n_arr[-1] != arr[i]:
        n_arr.append(arr[i])

print(n_arr)


# 다른 사람의 풀이
a =[]
print(a[-1:])
for i in arr:
    #리스트 형태는 null 값이여도 오류 발생하지 않는다, a[-1:]이 핵심
    if a[-1:] == [i] : continue
    a.append(i)

print(a)