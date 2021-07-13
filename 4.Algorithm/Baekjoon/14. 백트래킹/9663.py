# 9663

# python은 시간초과 pypy3로는 통과됨
N = int(input())
# 방문 리스트를 행, 대각선, 대각선 각각 만들어줌
row, diag1, diag2 = [0] * N, [0] * (2 * N - 1), [0] * (2 * N - 1)


def backtrack(i):
    global cnt

    # 모든 탐색에 성공했다면 카운트하기
    if i == N:
        cnt += 1
        return

    for j in range(N):
        # 값 있는지 확인 하나라도 있으면 안됨
        if row[j] or diag1[i + j] or diag2[j - i]:
            continue

        row[j] = diag1[i + j] = diag2[j - i] = 1  # 방문체크
        backtrack(i + 1)  # 재귀
        row[j] = diag1[i + j] = diag2[j - i] = 0  # 방문취소

cnt = 0
backtrack(0)
print(cnt)



# 다른 풀이
N = int(input())
# 방문 리스트를 행만 이용해서 확인할 수 있음
row = [0] * N


def check(x):
    for j in range(x):
        # 행이 같음 or 대각선이 같음을 이렇게 표현할 수 있다. 둘 중 하나가 같으면 false
        if row[x] == row[j] or abs(row[x] - row[j]) == x - j:
            return False
    return True


def backtrack(x):
    global cnt

    # 모든 탐색에 성공했다면 카운트하기
    if x == N:
        cnt += 1
        return

    for j in range(N):
        row[x] = j
        # 체크가 true라면 다음으로 진행
        if check(x):
            backtrack(x + 1)


cnt = 0
backtrack(0)
print(cnt)
