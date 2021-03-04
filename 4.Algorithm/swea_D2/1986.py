T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counter = [0]*N
    
    # counter라는 리스트에 번호를 1부터 N까지 나열
    for i in range(len(counter)):
        counter[i] += i+1
    
    # 짝수 인덱스에 있는 값은 더하고
    # 홀수 인덱스에 있는 값은 빼기
    total = 0
    for j in range(len(counter)):
        if j % 2 == 0:
            total += counter[j]
        elif j % 2 == 1:
            total -= counter[j]
    print('#{} {}'.format(tc, total))