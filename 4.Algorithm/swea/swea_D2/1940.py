# 입력으로 매 초마다 아래와 같은 command 가 정수로 주어진다.

# 0 : 현재 속도 유지.
# 1 : 가속
# 2 : 감속

# 위 command 중, 가속(1) 또는 감속(2) 의 경우 가속도의 값이 추가로 주어진다.
# N 초 동안 이동한 거리를 계산하는 프로그램을 작성하라.

# RC 카의 초기 속도는 0 m/s 이다.
# 현재 속도보다 감속할 속도가 더 클 경우, 속도는 0 m/s 가 된다.
# 테스트 케이스 첫 줄에는 Command 의 수 N이 주어지고, 둘째 줄부터, 매 줄마다 각각의 Command가 주어진다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    total = 0
    speed = 0
    #이해가 안되었던 문제,,,
    #숫자가 2개 주어지면 첫번째는 command 두번째는 속도이다
    #속도는 0부터 시작이며 command가 1이면 b가 속도에 더해지고, 2이면 속도가 b보다 작으면 속도는 0이되고 그렇지 않으면 속도에서 -b가 된다.
    for i in range(N):
        v = list(map(int, input().split()))
        #command, 즉 첫번때 인덱스가 1과 2일때 조건을 달아준다.
        if v[0] == 1:
            #가속(command = 1)이면 속도를 더해주고, 감속(command = 2)이면 속도와 b를 비교해서 값이 0이 되거나 속도를 감소시킨다.
            speed += v[1]
        elif v[0] == 2:
            if speed < v[1]:
                speed = 0
            else:
                speed -= v[1]
        total += speed
    print('#{} {}'.format(tc, total))