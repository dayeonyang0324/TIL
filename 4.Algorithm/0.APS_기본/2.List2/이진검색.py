# 중앙 값을 기준으로 중앙의 왼쪽에 있는지 오른쪽에 있는지 판단한다
# 없는 곳은 범위를 버려버리고 남은 위치의 절반을 또 다시 잡고 판단한다
# 업다운 게임이랑 똑같음.


def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False


# 재귀함수로 풀기
def binarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            return binarySearch2(a, low, middle - 1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle + 1, high, key)