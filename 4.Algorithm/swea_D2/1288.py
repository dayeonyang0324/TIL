

T = int(input())
for tc in range(1, T+1):
    N =input()
    #0부터9의 수가 나와야하기 때문에 counter을 만들었다.
    counter = [0]*10
    x = 0
    #N을 나열해야하기 때문에 문자열로 받았고 아래에서 계산을 위해 int로 변환해주어야 했다.
    #그런데 int(N)을 그대로 대입해주면 값이 이상하게 나왔다... 
    #intN이라는 새로운 변수를 지정해주어야 값이 제대로 나왔는데 왜 그런지 잘 모르겠다..
    intN = int(N)

    while 0 in counter:
        for j in N:
            #N이 문자열로 변경되어 있기 때문에 int값으로 다 수정해야함.
            if counter[int(j)] < 1:
                counter[int(j)] += 1
        x += 1
        N = str(intN * x)
    #1을 더한 후 while값이 멈추는 형태이므로 1을 빼주어야한다. 
    #아니면 x += 1과 새로 지정한 N을 for문 위로 옮겨주어야 한다.
    x -= 1
    print('#{} {}'.format(tc, x*intN))