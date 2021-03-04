
def bubble_sort(num):
    for i in range(len(num)-1, -1, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]


T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    bubble_sort(num)  # bubble_sort를 사용해서 정렬해주기(내장함수 사용 X)

    mini = 987654321  # 최솟값 구하기(내장함수 사용 X)
    for i in num:
        if mini > i:
            mini = i

    maxi = 0  # 최댓값 구하기(내장함수 사용 X)
    for j in num:
        if maxi < j:
            maxi = j

    total = 0  # 전체의 합을 더하기
    for i in num:
        total += i

    # round 사용해서 소숫점 첫째자리에서 반올림, total에 최대 최소 빼고 길이에서 두개 뺀만큼으로 나눔
    print('#{} {}'.format(tc, round((total-mini-maxi)/(len(num)-2))))