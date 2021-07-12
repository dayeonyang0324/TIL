# 15651

N, M = map(int, input().split())
result = []

def back():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N+1):
        # 15649, 15650 문제와 다른점은 리스트에 값이 있는지 확인하지 않는것
        result.append(i)
        back()
        result.pop()

back()


# 다른풀이
N, M = map(int, input().split())
visit = [False] * N
result = []

def back(lenr, N, M):
    if lenr == M:
        print(*result)
        return

    for i in range(N):
        # if 문으로 결과에 값이 있는지 확인하지 않아도 됨
        visit[i] = True
        result.append(i+1)
        back(lenr+1, N, M)
        visit[i] = False
        result.pop()

back(0, N, M)
