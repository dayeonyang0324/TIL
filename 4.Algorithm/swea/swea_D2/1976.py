T = int(input())
for tc in range(1, T+1):
    time_list = list(map(int, input().split()))
    h1 = time_list[0]
    m1 = time_list[1]

    h2 = time_list[2]
    m2 = time_list[3]

    hour = (h1 + h2) % 12  # 12시 넘어가면 12로 나눈 몫
    minute = m1 + m2
    if minute >= 60:  # 60분 넘으면 시간은 1추가, 분은 나머지
        hour += minute//60
        minute = minute % 60

    print('#{} {} {}'.format(tc, hour, minute))