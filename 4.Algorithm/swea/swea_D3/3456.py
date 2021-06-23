
T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    # 딕셔너리 형태로 숫자들을 정렬
    dict = {}
    for num in nums:
        if num in dict.keys():
            dict[num] += 1
        else:
            dict[num] = 1

    # 가로, 세로는 2개씩 이거나 4개가 모두 같아야하므로
    for key, value in dict.items():

        # 값들이 홀수라면 그 값이 하나 더 추가되어야한다
        if value % 2 == 1:
            print('#{} {}'.format(tc, key))
