# 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.


# 처음에는 이런식으로 코드를 짰다.
# 하나하나 값을 계산하다보니 코드가 너무 난해했다.
T = int(input())
for tc in range(1, T + 1):
    day = list(map(int, input().split()))

    total = 0
    # 현재 달의 마지막 날까지 빼서 더해주고
    if day[0] == 4 or day[0] == 6 or day[0] == 9 or day[0] == 11:
        total += 30 - day[1]
    elif day[0] == 2:
        total += 28 - day[1]
    else:
        total += 31 - day[1]

    # 같은 달이 될때까지 30, 31을 더해주었다
    while day[0] != day[2]:
        day[0] += 1
        if day[0] == 4 or day[0] == 6 or day[0] == 9 or day[0] == 11:
            total += 30
        elif day[0] == 2:
            total += 28
        else:
            total += 31

    #while문이 한번 더 더해지기 때문에 2번째 달을 빼고 다시 2번째 달의 일을 더해주었다.
    if day[2] == 4 or day[2] == 6 or day[2] == 9 or day[2] == 11:
        total -= 31 
        total += day[3]
    elif day[2] == 2:
        total -= 28 
        total += day[3]
    else:
        total -= 31 
        total += day[3]

    print('#{} {}'.format(tc, total+1))



#그렇지만 아주 간단하게 딕셔너리를 이용해서 구할 수 있었다. 
#month를 key로 보고 day를 value로 봐서 차이만큼 더해주면 되었다. 
T = int(input())
for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    total = 0
    for i in range(m1, m2):
        if m1 == i:
            total += month[i] - d1 + 1
        else:
            total += month[i]
    total += d2

    print("#{} {}".format(tc, total))