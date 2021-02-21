#5만원 단위부터 10원까지 나눌 수 있도록 갯수를 세는 것이다.
#for문을 사용하면 인덱스를 -5부터 비교하면 되지만 예외가 많이 생기고 번거롭다
#while을 사용해서 간단하게 풀 수 있었고 dictionary를 사용해도 간단하게 풀 수 있다.
#돈의 마지막은 항상 0이라는 문제의 조건이 있었지만 input에는 달라서 그냥 무시하고 풀었다.

T = int(input())
for tc in range(1, T+1):
    money = int(input())
    cnt = [0] * 8
    don = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    while money >= 10:
        for i in range(8):
            cnt[i] += money // don[i]
            money = money % don[i]

    print('#{}'.format(tc))
    print(*cnt)