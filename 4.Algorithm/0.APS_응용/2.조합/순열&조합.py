def comb(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


an = [1, 2, 3]
tr = [0] * 2
comb(3, 2)

########################################
# 재귀 - 조합
arr = [1, 2, 3, 4, 5]
c = [0] * 3


def comb2(i, n, r):
    if i == r:
        print(c)
    else:
        for j in range(i, n-r+i+1):
            c[i] = arr[j]
            comb2(i+1, n, r)


n = 5
r = 3
comb2(0, n, r)

##########################################
# for문 - 조합
M = 5
A = [1, 2, 3, 4, 5]
for i in range(0, M-3+1):
    for j in range(i+1, M-2+1):
        for k in range(j+1, M-1+1):
            print(i, j, k)
            # print(A[i], A[j], A[k])


###########################################
# 순열
nums = [1, 2, 3]


def perm(idx, length):
    if idx == length:
        print(*nums)
    else:
        for changer in range(idx, length):
            nums[idx], nums[changer] = nums[changer], nums[idx]
            perm(idx+1, length)
            nums[idx], nums[changer] = nums[changer], nums[idx]


perm(0, 3)

###################################################################
# swap사용 순열


def swap(i, j):
    nums[i], nums[j] = nums[j], nums[i]


def perm(idx, length):
    if idx == length:
        print(*nums)
    else:
        for changer in range(idx, length):
            swap(idx, changer)
            perm(idx+1, length)
            swap(idx, changer)
