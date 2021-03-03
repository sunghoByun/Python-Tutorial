import sys

input = [7,10,1,5,3,6,4,8]

def makeProfit(input : list):
    sort_list = sorted(input)
    tp_left, tp_right = 0, len(input)-1

    while True:
        left = input.index(sort_list[tp_left])
        right = input.index(sort_list[tp_right])

        profit = sort_list[tp_right] - sort_list[tp_left]

        if left < right :
            return profit
        else :
            if sort_list[tp_right] - sort_list[tp_left +1] > sort_list[tp_right -1] - sort_list[tp_left]:
                tp_left +=1
            else :
                tp_right-=1


print(makeProfit(input))

def makeProfitBruteForce(input : list):
    profit = 0

    for i, price in enumerate(input):
        for j in range(i, len(input)):
            profit = max(profit, input[j]- price)

    return profit

print(makeProfitBruteForce(input))

def makeProfitGraph(input : list):
    profit = 0
    min_num = sys.maxsize

    for i, price in enumerate(input):
        min_num = min(min_num,price)
        profit = max(profit, price - min_num)

    return profit

print(makeProfitGraph(input))