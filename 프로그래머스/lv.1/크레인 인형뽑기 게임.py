board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    rows = len(board)
    cols = len(board[0])

    rev_board = []

    for j in range(cols):
        tmp = []
        for i in range(rows):
            tmp.append(board[i][j])

        rev_board.append(tmp)

    answer = [0]

    count = 0
    for move in moves:
        for dolls in rev_board[move - 1]:
            if dolls != 0:
                answer.append(dolls)
                rev_board[move - 1].remove(dolls)
                if answer[-1] == answer[-2]:
                    answer.pop()
                    answer.pop()
                    count += 2
                break
    return count
