T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    two = format(M, 'b')  # 이진수로 변환
    two_rev = two[::-1]
    cnt = 0
    result = 'OFF'
    # 뒤에서 부터 N 길이만큼 1이여야 하므로 전체 뒤집에서 앞에서부터 슬라이싱
    for i in range(len(two_rev[0:N])):
        if two_rev[i] == '1':
            cnt += 1
    if cnt == N:
        result = 'ON'

    print('#{} {}'.format(tc, result))