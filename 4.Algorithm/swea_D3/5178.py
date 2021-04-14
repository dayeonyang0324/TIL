T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]

    # 완전 이진 트리에 주어진 값을 넣기
    for i in range(M):
        table, num = map(int, input().split())
        tree[table] = num

    # 자식들 더해서 부모에 값 넣기
    while N > 0:
        # 오른쪽 없는 경우 바로 부모에 넣기
        if N % 2 == 0:
            tree[N//2] = tree[N]
            N -= 1
        else: # 왼, 오 있으면 더해서 부모에 넣기
            tree[N // 2] = tree[N] + tree[N-1]
            N -= 2

    print('#{} {}'.format(tc, tree[L]))