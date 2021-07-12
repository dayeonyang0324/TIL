# 15650

# 15649 문제와 유사
N, M = map(int, input().split())
visit = [False] * N  # 방문 확인
result = []  # 결과 목록 리스트

# 자신 이후의 요소들만 검사하기 위해 새로운 변수를 준다 (j)
def back(lenr, j, N, M):
    if lenr == M:
        print(*result)
        return

    for i in range(j, N):
        if not visit[i]:
            visit[i] = True
            result.append(i+1)
            back(lenr+1, i+1, N, M)
            visit[i] = False
            result.pop()

back(0, 0, N, M)


# 다른풀이
N, M = map(int, input().split())
visit = [False] * N  # 방문 확인
result = []
def back(j):
    if len(result) == M:
        print(*result)
        return

    for i in range(j, N+1):
        if i not in result:
            result.append(i)
            # 재귀호출은 for문의 다음 요소를 부르기 위해 i를 사용한다
            back(i+1)
            result.pop()

back(1)
