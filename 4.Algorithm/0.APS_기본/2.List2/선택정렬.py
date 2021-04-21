# k번째로 작은 원소를 찾는 셀렉션 알고리즘
def select(list, k):
    for i in range(0, k):
        minidx = i
        for j in range(i+1, len(list)):
            if list[minidx] > list[j]:
                minidx = j
        list[i]. list[minidx] = list[minidx], list[i]
    return list[k-1]

##########################################################
# 셀렉션 알고리즘을 전체에 적용한 선택정렬
# 리스트 처음에 있는 요소부터 비교하기 시작함.
# 뒤에 더 작은 요소가 있으면 '인텍스'를 갖고 교환함


def selectionsort(a):
    for i in range(0, len(a) - 1):
        minidx = i
        for j in range(i+1, len(a)):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]


# 예
arr = [10, 15, 2, 19, 6, 14]

for i in range(len(arr) - 1):
    min_idx = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # 첫번째는 [2, 15, 10, 19, 6, 14] 이렇게 두개의 값만 변한다.
print(arr)