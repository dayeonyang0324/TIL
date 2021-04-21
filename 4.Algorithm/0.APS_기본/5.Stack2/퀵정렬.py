

# 퀵 정렬 : 중앙값인 pivot을 설정해서 왼쪽은 pivot보다 크거나 같은 값, 오른쪽은 pivot보다 작은값을 선택
# 계속 비교하면서 L, R값을 찾아 교환한다. 둘다 해당하는 값이 없으면 pivot과 나머지 값과 교환한다.

# 1.
def quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quicksort(a, begin,p-1)
        quicksort(a, p+1, end)


def partition(a, begin, end):
    pivot = (begin + end)//2
    L = begin
    R = end

    while L < R:
        while (a[L] < a[pivot] and L < R):
            L += 1
        while (a[R] >= a[pivot] and L < R):
            R -= 1

        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]

    a[pivot], a[R] = a[R], a[pivot]

    return R


########################################################
# 2.
def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = (start + end) // 2
    left = start
    right = end

    # left와 right가 만날 때까지 반복
    while left < right:
        # 왼쪽 원소가 기준값보다 작으면 우측으로 이동
        while arr[left] < arr[pivot] and left < right:
            left += 1
        # 오른쪽 원소가 기준점보다 크면 좌측으로 이동
        while arr[right] >= arr[pivot] and left < right:
            right -= 1

        if left < right:
            # pivot 왼쪽 원소가 모두 pivot 보다 작으면
            if left == pivot:
                # pivot 변경
                pivot = right
            # 조건에 맞지 않는 left, right 값을 swap (else:)
            arr[left], arr[right] = arr[right], arr[left]

    # 반복문 종료 후 pivot과 right 자리의 원소 swap
    arr[pivot], arr[right] = arr[right], arr[pivot]

    # right 를 기준으로 좌측/우측 퀵 정렬
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)