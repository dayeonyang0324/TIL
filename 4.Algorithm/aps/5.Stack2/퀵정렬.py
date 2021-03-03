# 퀵 정렬 : 중앙값인 pivot을 설정해서 왼쪽은 pivot보다 크거나 같은 값, 오른쪽은 pivot보다 작은값을 선택
# 계속 비교하면서 L, R값을 찾아 교환한다. 둘다 해당하는 값이 없으면 pivot과 나머지 값과 교환한다.


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