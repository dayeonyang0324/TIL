# 2775
#
# 재귀 시간초과
# def people(n,m):
#     if n == 0:
#         return m
#     elif m == 1:
#         return 1
#     return people(n-1, m) + people(n, m-1)
#
#
# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     print(people(k, n))

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    apt = [i for i in range(1, n+1)]  # 0층에 사는 사람들

    # 해당 호는 그 전 층의 해당 호까지 합한 것
    # 3층 3호는 2층의 3호까지 합, 2층 각각 요소는 1층 호의 합을 더한것임
    for i in range(k):  # 계속 사람을 더해서 리스트를 리셋 -> 층만큼 for 문
        for j in range(1, n):  # 기존 호에 아래층 (내 아래 호 + 내 아래 왼쪽 호) 넣기
            apt[j] += apt[j-1]
    print(apt[n-1])  # 해당 호까지 구했으므로 마지막 요소랑 같음
