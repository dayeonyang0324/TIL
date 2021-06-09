# 1341
# 1291 문제와 유사한 문제
s, e = map(int, input().split())

if s >= e:
    for i in range(s, e-1, -1):
        cnt = 0
        for j in range(1, 10):
            # 수식 간의 사이 공백은 3칸이어야 함. \t는 안됨..
            print('{0} * {1} = {2:2}'.format(i, j, i*j), end='   ')
            # 한줄에 3개씩 출력하기 위해 cnt 변수를 주어 3개가 되면 다음줄로 내려가도록 했다.
            cnt += 1
            if cnt == 3:
                print()
                cnt = 0
        print()
else:
    for i in range(s, e+1):
        cnt = 0
        for j in range(1, 10):
            print('{0} * {1} = {2:2}'.format(i, j, i * j), end='   ')
            cnt += 1
            if cnt == 3:
                print()
                cnt = 0
        print()