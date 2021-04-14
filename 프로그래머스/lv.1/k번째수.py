array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
def solution(array,commands):
    result = []
    for command in commands:
        new_arr =[]
        new_arr = array[command[0]-1:command[1]]
        new_arr.sort()
        result.append(new_arr[command[2]-1])

    print(result)