
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    maxi = 0
    total = 0
    for i in range(N-1, -1, -1):  # 뒤에서부터 판단하기
        if maxi < num[i]:  # 최댓값이라면 최댓값이라고 저장해주고
            maxi = num[i]
            total += (maxi - num[i])
        else:
            total += (maxi - num[i])  # 현재 값이 최댓값보다 작으면 빼서 더해주기
    print('#{} {}'.format(tc, total))