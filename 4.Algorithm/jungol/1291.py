# 1291

"""
1 6 // ERROR 출력
2 4 // 2, 4단 출력
"""

# 조건을 만족하지 않으면 다음 input을 받아야 하기 때문에 while문 사용
while True:
    # EOF오류를 해결하기 위해 try-except 사용
    try:
        s, e = map(int, input().split())

        # 2~9 범위에 있지 않다면 에러 출력
        if s > 9 or e > 9 or s < 2 or e < 2:
            print('INPUT ERROR!')

        # 범위에 있다면 오름차순인지 내림차순인지 구분
        else:
            if s >= e:
                for i in range(1, 10):
                    for j in range(s, e-1, -1):
                        # 자릿수 맞추기 위해 {}안에 값 주기, end 줘서 3칸 띄고 다음 구구단 출력
                        # 이부분이 가장 오래 걸렸음..
                        print('{0} * {1} = {2:2}'.format(j, i, i*j), end='   ')
                    print()
            else:
                for i in range(1, 10):
                    for j in range(s, e+1):
                        print('{0} * {1} = {2:2}'.format(j, i, i * j), end='   ')
                    print()
    except:
        break