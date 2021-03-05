
T = int(input())
for tc in range(1, T+1):
    health = list(map(int, input().split()))
    print('#{}'.format(tc), end=' ')

    # 받은 리스트의 0번째는 최소값, 1번째는 최댓값, 2번쨰는 실제 운동량이다
    if health[0] <= health[2] <= health[1]: # 사이에 맞게 운동했으면 0 출력
        print(0)
    else:
        if health[2] > health[1]:  # 초과되었으면 -1 출력
            print(-1)
        elif health[2] < health[0]:
            print(health[0]-health[2])  # 부족하면 최솟값 - 현재량
