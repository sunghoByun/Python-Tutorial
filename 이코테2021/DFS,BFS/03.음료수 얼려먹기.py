# N, M  = 4, 5
# graph = [
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0]
# ]

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

def solution(N, M, graph):
    def dfs(row, col, graph):
        if row >= 0 and col >= 0 and row < N and col < M :
            if graph[row][col] == 0 :
                graph[row][col] = 1
                # print(row,col)
                dfs(row-1, col, graph)
                dfs(row+1, col , graph)
                dfs(row, col-1, graph)
                dfs(row, col+1, graph)
                return True
            else : return False
        else : return False

    count = 0

    for row in range(N):
        for col in range(M):
            if dfs(row,col, graph) :
                count+=1

    return count

print(solution(N,M,graph))
