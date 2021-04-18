a = 5
b = 24

def solution( a:int, b:int):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" ]
    date = 0

    # for i in range(a-1):
    #     date += months[i]
    date = sum(months[:a-1])
    date += b

    return days[date%7]

# print(solution(5,24))


