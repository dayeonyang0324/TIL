# 2750

# 버블 정렬 : 시간복잡도 O(n^2)
# 리스트 뒤에서부터 인접한 값과 비교하며 바꾸는 방식
def bubble_sort(N, num):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]


"""
3 2 1

2 3 1
2 1 3

1 2 3
"""

N = int(input())
num = list(int(input()) for _ in range(N))
bubble_sort(N, num)
for i in range(N):
    print(num[i])
