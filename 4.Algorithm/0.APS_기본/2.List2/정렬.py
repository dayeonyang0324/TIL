

# list a가 정렬되어 있지 않은 경우
def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
        if i < n:
            return i
        else:
            return -1


# list a가 정렬되어 있는 경우
def sequentialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
        if i < n and a[i] == key:
            return i
        else:
            return -1


#####################################
# 예
arr = [4, 9, 11, 23, 19, 7]

key = 23

for i in range(len(arr)):
    if key == arr[i]:
        print(i)
        break
else:
    print('0')


# 예
arr = [4, 7, 9, 11, 19, 23]

key = 23

for i in range(len(arr)):
    if key == arr[i]:
        print(i)
        break
    elif key < arr[i]:
        print(i)
        break
else:
    print('0')
