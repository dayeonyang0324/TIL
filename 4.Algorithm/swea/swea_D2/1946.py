#A 10
#B 7
#C 5

#AAAAAAAAAA
#BBBBBBBCCC
#CC

#압축을 풀었을 때 다음과 같이 한줄에 10개씩 나열, 10개가 넘어가면 다음줄로 넘어가도록 복사한다.
T = int(input())
for tc in range(1, T + 1):
    kinds = int(input())
    
    #먼저 test case를 복사하고 줄바꿈은 sep='|n'을 사용한다.(중요!!)
    print('#{}'.format(tc), sep='|n')
    new = ''
    for kind in range(kinds):
        a, b = input().split()
        new += a * int(b)

    #처음에는 while문을 사용하고 싶었는데 그럼 조건문을 또 활용해야해서 
    #간단한 for문을 사용해서 프린트 할 수 있었다.
    #여기서도 sep='|n'을 사용해서 쉽게 줄바꿈을 할 수 있었다.
    #슬라이싱을 하면 잘리고 남은 요소들, 10까지 잘랐으면 11이 인덱스 0으로 오지 않는다!
    #그렇기 떄문에 for문이나 조건문 등 활용해야하고 for문을 사용해서 i값을 10씩 띄어주면 된다.
    for i in range(0, len(new), 10):
        print(new[i:i+10], sep='|n')
