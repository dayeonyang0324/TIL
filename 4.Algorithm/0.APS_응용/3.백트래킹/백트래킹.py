# 백트래킹 swea_5209
# 가능한 모든 경로를 탐색하되, 유망하지 않다면 탐색하지 않고 부모 노드로 돌아가 탐색을 진행한다
# 시간 단축에 좋음 (예, N-queens 문제)


def backtrack(i, total):
    global result

    # 최종 결과값 result, 중간 결과값 total -> 최소값 찾아야하므로 더 이상 보지 않음
    if total > result:
        return

    # 끝까지 다 도달한 후에 최종결과값이 현재 결과값보다 크다면 현재 결과값이 최종결과값
    if i == N:
        if result > total:
            result = total
        return

    # 방문한적 있는지 체크, 없다면 방문하고 중간결과값에 값 더하기
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            backtrack(i + 1, total + table[i][j])
            visited[j] = 0


# 방문처리할 리스트와 결과값 비교를 위한 값이 필요함
N = int(input())
result = 1234567890
visited = [0] * N
table = [[input()] for _ in range(N)]

# 목록중에 최솟값 출력
backtrack(0, 0)