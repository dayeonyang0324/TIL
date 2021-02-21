T = int(input())
for tc in range(1, T+1):
    N = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #문자열 길이가 다르므로 두가지 케이스를 나눠서 생각해야 한다.
    if len(A) < len(B):
        sum_list = []
        #짧은 길이가 움직이므로 긴길이에서 뺀만큼 이동해야한다. 
        for i in range(len(B) - len(A) + 1):
            total = 0
            #대응되는 두값들이 곱해서 더해지고 짧은 길이가 이동하면서 계산을 반복한다.
            #두번째 for문이 한바퀴 돌고 i값이 변화해야하므로 total값은 첫번째 for문 이후에 들어가야 한다.
            for j in range(len(A)):
                total += A[j] * B[j + i]
            sum_list.append(total)

        #리스트에서 최대값을 구한다.
        maxi = 0
        for sum_num in sum_list:
            if sum_num > maxi:
                maxi = sum_num

    if len(A) > len(B):
        sum_list = []
        for i in range(len(A) - len(B) + 1):
            total = 0
            for j in range(len(B)):
                total += B[j] * A[j + i]
            sum_list.append(total)

        maxi = 0
        for sum_num in sum_list:
            if sum_num > maxi:
                maxi = sum_num


    print('#{} {}'.format(tc, maxi))