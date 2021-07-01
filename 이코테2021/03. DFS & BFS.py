from collections import deque

# def bfs(graph, start, visited):
#      queue = deque(start)
#     visited[start] = True
#
#     while queue:
#         v = queue.popleft()
#         print(v, end='->')
#
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited= [False] * 9



def bfs(graph, v, visited):
    queue = deque([v]) #시작 노드로 큐 생성
    visited[v] = True #시작 노드 방문

    while queue: #모두 방문할 때 까지
        i = queue.popleft() #pop
        for j in graph[i]: # pop 한 노드와 연결된 모든 노드들 loop
            if not visited[j] : # 연결된 노드가 아직 방문하지 않았다면
                visited[j]  = True #해당 노드 방문처리
                queue.append(j) #queue에 넣고 이따가 이 노드와 연결된 모든 리스트도 탐색 예정

def bfs2(graph, v, visited):
    queue = deque([v]) #시작 노드로 큐 생성
    visited[v] = True

    while queue: # 작업 큐 끝날때까지 loop
        i = queue.popleft() # 탐색 노드 pop
        print(i, end='->')
        for j in graph[i]: #탐색 노드와 연결된 모든 노드 loop
            if not visited[j]: #연결된 노드 아직 탐색하지 않았다면
                visited[j] = True
                queue.append(j)

def DFS(graph, v, visited):
    visited[v] = True # 첫 노드 방문처리
    print(v, end = '->')
    for i in graph[v]: #첫 노드의 인접노드들 중
        if not visited[i]: # 방문하지 않은 노드가 있다면
            DFS(graph, i, visited) #스택 형식으로 방문 처리

# bfs2(graph,1,visited)
DFS(graph,1,visited)