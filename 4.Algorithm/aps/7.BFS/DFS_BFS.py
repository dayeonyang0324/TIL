# 백준 문제 NO.1260
import sys
sys.stdin = open('input.txt')


# DFS 풀이
def dfs(G):
    visited = [False for _ in range(n+1)]
    to_visit = [v]
    result = []

    while to_visit:
        now = to_visit.pop()
        if not visited[now]:
            visited[now] = True
            result.append(now)
            to_visit += reversed(sorted(G[now]))

    return result


# BFS 풀이
def bfs(G):
    visited = [False for _ in range(n + 1)]
    to_visit = [v]
    result = []

    while to_visit:
        now = to_visit.pop(0)
        if not visited[now]:
            visited[now] = True
            result.append(now)
            to_visit += sorted(G[now])

    return result


T = int(input())
for tc in range(1, T+1):
    n, m, v = map(int, input().split())
    nod = [list(map(int, input().split())) for _ in range(m)]
    G = [[] for _ in range(n+1)]
    for i in range(m):
        start = nod[i][0]
        end = nod[i][1]
        G[start].append(end)
        G[end].append(start)

    print(*dfs(G))
    print(*bfs(G))



