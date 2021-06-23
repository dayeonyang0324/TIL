T = int(input())
for tc in range(1, T+1):
    n = int(input())
    table = [list(input().split()) for _ in range(n)]
    print('#{}'.format(tc))

    # 90도 회전
    result90 = []
    for i in range(n):
        result = []
        for j in range(n):
            result.append(table[n-1-j][i])
        result90.append(result)

    # 180도 회전
    result180 = []
    for i in range(n):
        result = []
        for j in range(n):
            result.append(table[n-1-i][n-1-j])
        result180.append(result)

    # 270도 회전
    result270 = []
    for i in range(n):
        result = []
        for j in range(n):
            result.append(table[j][n-1 - i])
        result270.append(result)

    for i in range(n):
        print(''.join(result90[i]), ''.join(result180[i]), ''.join(result270[i]))