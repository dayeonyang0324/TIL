# 2751 - PyPy3로 제출해야함

N = int(input())
num = list(int(input()) for _ in range(N))


for i in sorted(num):
    print(i)

# 퀵정렬 : 시간복잡도 O(nlogn)
# def quick_sort(a, begin, end):
#     if begin < end:
#         p = partition(a, begin, end)
#         quick_sort(a, begin, p-1)
#         quick_sort(a, p+1, end)
#
#
# def partition(a, begin, end):
#     pivot = begin
#     L = begin + 1
#     R = end
#
#     while L <= R:
#         while a[L] < a[pivot] and L <= R:
#             L += 1
#         while a[pivot] <= a[R] and L <= R:
#             R -= 1
#
#         if L < R:
#             if L == pivot:
#                 pivot = R
#             a[L], a[R] = a[R], a[L]
#
#     a[pivot], a[R] = a[R], a[pivot]
#
#     return R
#
#
# quick_sort(num, 0, N-1)
# for i in range(N):
#     print(num[i])
