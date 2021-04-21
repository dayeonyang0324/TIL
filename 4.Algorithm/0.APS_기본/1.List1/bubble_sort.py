
# 버블 정렬은 리스트의 인접한 값을 비교하면서 오름차순으로 정리한다.
# 뒤에부터 큰 값이 정렬되고 다시 앞으로 돌아와 똑같은 사이클을 [0]이 남기 전까지 돌린다.
# [7 4 1] -> [4 7 1] -> [4 1 7] -> [1 4 7]


def Bubble_sort(a):  # 정렬할 list
    for i in range(len(a)-1, 0, -1):  # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


arr = [55, 7, 78, 12, 42]
Bubble_sort(arr)

print(arr)