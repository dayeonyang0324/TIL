#최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    

    #점수는 0점부터 100점까지이므로 101개의 칸을 만들어 점수에 해당하는 인덱스를 1씩 증가시킨다
    counter = [0]*101
    for i in score:
        counter[i] += 1

    #가장 큰 인덱스값을 구하면 최빈도를 쉽게 구할 수 있지만 같은 값이라면 큰 점수를 출력해야한다.
    # 이미 counter를 통해 점수 순서대로 나열되어 있으며 for문을 뒤(높은 점수)부터 돌리면 된다!!
    maxi = 0
    high = 0
    for j in range(len(counter)-1, -1, -1):
        if maxi < counter[j]:
            maxi = counter[j]
            high = j
    print('#{} {}'.format(tc, high))                
        