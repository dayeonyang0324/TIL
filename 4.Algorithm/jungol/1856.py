# 1856
n, m = map(int, input().split())

for i in range(n):
    # 짝수 인덱스 행의 경우 순서대로 수가 증가한다
    if i % 2 == 0:
        for j in range(1, m+1):
            print((m*i)+j, end=' ')
    # 홀수 인덱스 행의 경우 -1씩 내림차순한다
    else:
        for j in range(m, 0, -1):
            print((m * i) + j, end=' ')
    print()