T = int(input())
for tc in range(1, T+1):
    time_list = list(map(int, input().split()))
    h1 = time_list[0]
    m1 = time_list[1]

    h2 = time_list[2]
    m2 = time_list[3]

    hour = (h1 + h2) % 12
    minute = m1 + m2
    if minute >= 60:
        hour += minute//60
        minute = minute % 60

    print('#{} {} {}'.format(tc, hour, minute))