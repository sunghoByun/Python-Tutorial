name = "AAAA"

def solution(name):
    min_move = len(name) - 1
    answer = 0
    for i, chr in enumerate(name):
        answer += min(ord('Z') - ord(chr)+1, ord(chr) - ord('A'))

        next = i +1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i + i + len(name) - next)

    answer += min_move
    return answer

print(solution("AAA"))

# for a in name:
#     cnt = min()
#     print(cnt)
