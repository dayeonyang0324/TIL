# 10250

T = int(input())
for _ in range(1, T+1):
    H, W, N = map(int, input().split())  # 호텔 층, 호 수, 손님

    # 호텔의 왼쪽 아래부터 위로 올라가면서 배정된다
    # 손님 순서를 층으로 나눠진 몫이 호수가 되고, 층으로 나눠진 나머지 +1이 층이된다
    floor = N % H
    line = N // H + 1
    # 나머지가 0이면 꼭대기 층일때 이므로 따로 설정해준다
    if floor == 0:
        floor = H
        line -= 1
    # 호수는 한자리일떄 앞에 0이 붙어야한다.(다른경우는 층 * 100 + 호수)
    print('%d''%02d' % (floor, line))
