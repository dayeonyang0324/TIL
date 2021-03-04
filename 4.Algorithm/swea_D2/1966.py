# 숫자를 오름차순으로 정렬하는 문제는 bubble sort를 활용해 풀 수 있다.
# bubble sort는 맨 첫번째 값이 마지막까지 비교를 거쳐야해서 i가 큰 수부터 시작된다.


def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    bubble_sort(num)
    
    print('#{}'.format(tc), *num)