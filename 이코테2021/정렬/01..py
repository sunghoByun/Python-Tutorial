#부품 찾기
#
# n = int(input())
# nn = list(map(int, input().split()))
#
# m = int(input())
# mm = list(map(int, input().split()))

n = 5
nn = [8,3,7,9,2]
m = 3
mm = [5,7,9]
nn.sort()



def gyaesuSort(n, nn, m, mm):
    new_nn = set(nn)

    nn_list = [0] *(max(new_nn)+1)

    for N in nn :
        nn_list[N] = 1

    for M in mm:
        if nn_list[M] == 1 :
            print("yes", end = " ")
        else:
            print("no", end = " ")

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return "yes"
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    return "no"

# for M in mm:
#     print(binary_search(nn, M, 0, n), end = ' ')


