
# 모든 칸에서 하얀 부분을 예외로 잡기

def exc(table):
    exc_total = 0
    for i in range(N//2):
        for j in range(N//2-i):
            exc_total += table[i][j]
            exc_total += table[N-1-i][N-1-j]
            exc_total += table[N-1-i][j]
            exc_total += table[i][N-1-j]

    return exc_total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input())) for _ in range(N)]
    
    # 모든 칸을 다 더하고 예외인 하얀 칸을 빼주기
    total = 0
    for i in range(N):
        for j in range(N):
            total += table[i][j]

    print('#{} {}'.format(tc, total-exc(table)))
