# 너비 우선 탐색


def BFS(G, N, v):  # 그래프 G, 탐색 시점 v
    visited = [0] * N  # 정점의 갯수 만큼
    queue = [v]  # v가 시작점인 큐 생성

    while queue:  # 큐가 비어있지 않을 경우
        t = queue.pop(0)  # 큐의 첫번째 원소 반환
        if not visited[t]:  # 방문되지 않은 곳이라면
            visited[t] = True  # 방문한 것으로 표시
            # visit(t)

        # queue += G[t] 이렇게 쓰거나 아래와 같이 쓰기
        for i in G[t]:  # t와 연결된 모든 선에 대해
            if not visited[i]:  # 방문하지 않은 곳이라면
                queue.append(i)  # 큐에 넣기

#########################################################
# 불필요한 데이터 값들 최소화


def BFS2(G, N, v):  # 그래프 G, 탐색 시점 v
    visited = [0] * N  # 정점의 갯수 만큼
    queue = [v]  # v가 시작점인 큐 생성
    visited[v] = True  # 방문하기 전에 체크, 중복 방지

    while queue:  # 큐가 비어있지 않을 경우
        t = queue.pop(0)  # 큐의 첫번째 원소 반환
        for i in G[t]:  # t와 연결된 모든 선에 대해
            if not visited[i]:  # 방문하지 않은 곳이라면
                queue.append(i)  # 큐에 넣기
                visited[i] = True  # 이미 들어가있다면 넘어가는 방식
