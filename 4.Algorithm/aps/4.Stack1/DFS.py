# DFS 탐색하는 방법 2가지

# 1. global result를 사용하는 방법
# table은 2차원 리스트 형태로 점사이 edge가 있는지 확인할 수 있음

def DFS(S, G, V, table):
    global result
    #저장할 리스트 만들어줌
    visited = [0]*(V+1)
    visited[S] = 1
    for i in range(1, V+1):
        if table[S][i] and not visited[i]:
            if i == G:
                result = 1
                return
            DFS(i)
# 4871 그래프 경로 문제


####################################################################


# 2. True, False를 바꾸면서 탐색하는 방법
# 그래프(G)는 딕셔너리 같은 리스트 형태로 들어감.
# 리스트 안의 리스트의 인덱스가 점들이고 리스트 값들이 연결된 점을 나타냄

def solution(G):
    visited = [False for _ in range(100)]  # 노드의 갯수 만큼 F로 채워진 리스트 만듦
    to_visits = [0]  # 현재 위치 즉 출발지점을 입력함 = stack

    while to_visits:  # stack안에 요소들이 있을때 계속 반복
        now = to_visits.pop()  # 현재 위치는 stack.pop한 값
        # 완전 탐색은 아닌 코드
        # if now == 99:
        #     return 1
        if not visited[now]:  # 아직 가지 않은 False의 상태라면,
            visited[now] = True  # 가고 True로 바꿈
            to_visits += G[now]  # stack에 현재 위치가 갈 수 있는 요소들을 추가

    return int(visited[99])  # 가야하는 노드에 갔는지 안갔는지 출력
# 1219 길찾기 문제
