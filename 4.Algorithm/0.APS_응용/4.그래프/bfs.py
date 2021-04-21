# bfs 구현하기
# def bfs(g, v): # 그래프, 탐색 시작점
#     큐 생성
#     시작점 v를 큐에 삽입
#     점 v를 방문한 것으로 표시
#     while 큐가 비어있지 않은 경우
#         t = 큐의 첫번째 원소 반환
#         for t와 연결된 모든 선에 대해
#             u = t의 이웃점
#             u가 방문되지 않은 곳이라면
#             u를 큐에 넣고 방문한 곳으로 표시

'''
5 6
1 2 1 3 3 2 3 4 2 5 5 4
'''

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0] * (V+1) for _ in range(V+1)]
adjlist = [[] for _ in range(V+1)]

for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1  # 인접
    adjlist[n1].append(n2)


def bfs(s, V):  # 시작점 s, 정점 개수 V
    Q = [s]  # 큐 생성, 시작점 인큐
    visited = [0] * (V+1)
    visited[s] = 1
    while Q:  # front != rear
        t = Q.pop(0)
        print(t)  # visit(t)
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = visited[t] + 1  # 몇 번 갔는지 한번에 알 수 있음


bfs(1, V)


# dfs 재귀 참고
# def dfs(g, v):
#     if v = goal
#         cnt ++
#     else:
#         visited[v] = True  # v 방문설정
#
#     for each all w in adjacency(g, v)
#         if visited[w] != True
#             dfs(g, w)
#     visited[v] = False