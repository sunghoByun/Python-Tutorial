n  = 6
times = [7,10]

left, right = 1, max(times) * n
answer = 0

while left <= right:
    mid = (left + right) //2
    temp = 0
    for time in times:
        temp += mid//time
    if temp >= n :
        right = mid
    else :
        left = mid +1

print(right)