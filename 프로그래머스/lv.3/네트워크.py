from collections import deque

n = 3
computers = [[1,1,0],[1,1,0],[0,0,1]]

from collections import deque

def solution(n, computers):
    visited = [False] * n

    def BFS(computers, n, visited):
        queue = deque([n])  # 첫 노드로 큐 생성

        while queue:
            i = queue.popleft()  # 방문할 노드 pop
            for j in range(len(computers[i])):  # 방문할 노드와 인접한 노드 탐색 loop
                if j == i:
                    continue  # 본인 노드 제외
                elif computers[i][j] == 1:  # 연결된 다른 노드가 있다면
                    queue.append(j)  # 해당 노드도 큐에 넣음
                    computers[i][j] = 0
                    computers[j][i] = 0
                    visited[i] = True
                    visited[j] = True

    answer = 0
    for i in range(n):
        if not visited[i]:
            BFS(computers, i, visited)
            answer += 1

    return answer

def solution2(n, computers):
    answer = 0
    visited = [0 for i in range(n)] #방문 기록 리스트 생성
    def dfs(computers, visited, start):
        stack = [start] #작업 스택 생성
        while stack: # 작업 스택 반복 loop
            j = stack.pop() # 작업 노드 pop
            if visited[j] == 0: # 해당 노드 방문 확인 후
                visited[j] = 1 # 방문 체크

            for i in range(0, len(computers)): #j 그래프 노드 반복 loop
                if computers[j][i] ==1 and visited[i] == 0: #네트워크가 연결되어 있고, 아직 방문하지 않은 노드라면
                    stack.append(i) #해당 노드 추가
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer

print(solution2(n,computers))