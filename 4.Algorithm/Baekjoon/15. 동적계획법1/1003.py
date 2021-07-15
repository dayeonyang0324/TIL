# 1003


T = int(input())
for _ in range(T):
    N = int(input())
    start = [(1, 0), (0, 1)]  # 0, 1일때 값을 초기값으로 지정
    for i in range(2, N + 1):  # 재귀문을 for문을 사용해 append 해준다
        start.append((start[i - 1][0] + start[i - 2][0], start[i - 1][1] + start[i - 2][1]))
    print(*start[N])


# 시간초과 문제
# T = int(input())
# for _ in range(T):
#     N = int(input())
#
#     def sol(N):
#         if N == 0:
#             return [1, 0]
#         elif N == 1:
#             return [0, 1]
#         return [sol(N-1)[0] + sol(N-2)[0], sol(N-1)[1] + sol(N-2)[1]]
#
#     print(*sol(N))


"""
  0 1 2 3 4 5
0 1 0 1 1 2 3
1 0 1 1 2 3 5
"""