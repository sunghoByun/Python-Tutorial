import heapq as h

scoville = [1, 2, 3, 9, 10, 12]
K = 7

h.heapify(scoville)
answer = 0
print(scoville)
print("start")
while True:
    min1 = h.heappop(scoville)
    print(scoville)
    if min1 >= K:
        break
    elif len(scoville) == 0 :
        answer = -1
        break
    min2 = h.heappop(scoville)
    new_scovile = min1 + min2*2
    h.heappush(scoville, new_scovile)
    answer +=1

print(answer)