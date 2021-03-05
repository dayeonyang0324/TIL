
for _ in range(1, 11):
    tc = int(input())
    n, m = map(int, input().split())

    # n을 m번 곱하기
    total = 1
    for i in range(m):  # for문 사용해서 n을 곱해주기
        total *= n

    print('#{} {}'.format(tc, total))