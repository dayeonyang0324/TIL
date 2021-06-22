T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    cnt = 0
    move = y - x

    if move == 1:
        cnt = 1
    elif move == 2:
        cnt = 2
    elif move >= 3:
        pass

    print(cnt)

    """
    1 1

    2 11

    3 111
    4 121

    5 1211
    6 1221

    7 12211
    8 12221
    9 12321

    10 123211
    11 123221
    12 123321

    13 1233211
    14 1233221
    15 1233321
    16 1234321
    ...
    """
