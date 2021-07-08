# 10989

# counting_sort

# 메모리 초과 코드
# def counting(arr, N):
#     count_arr = [0] * (N+1)
#
#     for i in arr:
#         count_arr[i] += 1
#
#     for i in range(N):
#         count_arr[i+1] += count_arr[i]
#
#     result = [-1] * len(arr)
#
#     for i in arr:
#         result[count_arr[i] - 1] = i
#         count_arr[i] -= 1
#
#     for i in range(len(result)):
#         print(result[i])
#
#
# N = int(input())
# nums = [int(input()) for _ in range(N)]
# counting(nums, N)


import sys

N = int(sys.stdin.readline())
result = [0] * 10001 # 빈도 저장하기 위한 배열

# 수가 몇번 들어왔는지 카운팅
for i in range(N):
    a = sys.stdin.readline()
    result[int(a)] += 1

# 배열을 순회하며 저장된 횟수만큼 인덱스값을 출력
for j in range(1, 10001):
    if result[j] >= 1:
        for k in range(result[j]):
            print(j)
