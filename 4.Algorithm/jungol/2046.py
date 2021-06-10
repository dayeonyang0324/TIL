# 2046

n, m = map(int, input().split())

# m에 따라 출력되는 종류가 다르다
# 1일때는 행은 반복, 열은 수 증가
if m == 1:
    for i in range(1, n+1):
        for j in range(n):
            print(i, end=' ')
        print()

# 2일때는 홀수 짝수 행에 따라 오름차순, 내림차순 출력
elif m == 2:
    for i in range(1, n+1):
        if i % 2 == 0:
            for j in range(n, 0, -1):
                print(j, end=' ')
            print()
        else:
            for j in range(1, n+1):
                print(j, end=' ')
            print()

# 3일때는 첫 행만 오름차순이고 다음 열 부터는 배수가 나열된다
elif m == 3:
    for i in range(1, n+1):
        if i == 1:
            for j in range(n):
                print(i + j, end=' ')
            print()
        else:
            for j in range(1, n+1):
                print(i * j, end=' ')
            print()
