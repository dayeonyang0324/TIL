# 1018

# 주어진 배열 중에 임의의 8*8을 선택해서 바꿔야하는 칸의 최솟값
M, N = map(int, input().split())
table = [input() for _ in range(M)]

result = []
for i in range(M-7):
    for j in range(N-7):
        idx1 = 0
        idx2 = 0
        # 주어진 배열을 8개씩 나눠서 탐색하는 for문
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 이해가 잘 안감..
                # 합이 짝수일때 == (0,0)부터 시작하는 대각선
                if (k+l) % 2 == 0:
                    if table[k][l] == 'B':
                        idx1 += 1
                    elif table[k][l] == 'W':
                        idx2 += 1
                # 다른 대각선
                else:
                    if table[k][l] == 'W':
                        idx1 += 1
                    elif table[k][l] == 'B':
                        idx2 += 1
        result.append(idx1)  # 'B'의 갯수
        result.append(idx2)  # 'W'의 갯수
        # print(idx1, idx2)

print(min(result))
