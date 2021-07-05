# 11729

# 하노이탑 이동 경로 함수
# 1, 2, 3번째 탑을 s, m, e라 한다
def hanoi(N, s, m, e):
    if N == 1:
        print(s, e)
    else:
        hanoi(N-1, s, e, m)
        print(s, e)
        hanoi(N-1, m, s, e)


N = int(input())
print((2 ** N) - 1)
hanoi(N, 1, 2, 3)
