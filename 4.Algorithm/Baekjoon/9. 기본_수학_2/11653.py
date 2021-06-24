# 11653

N = int(input())
# 2부터 시작해서 N이 1이 될떄까지 나누기
i = 2
while N != 1:
    if N % i == 0:
        # 나눠지면 출력하고 그 나머지를 다시 나누기
        print(i)
        N = N // i
    else:
        # 나눠지지 않으면 값 증가해서 나눠보기
        i += 1

# 약수에서 소수를 찾고 소수를 N이 1이 될때까지 나눠 출력 -> 시간초과\
# 약수 찾기
# factors = []
# for i in range(2, N):
#     while True:
#         if N % i == 0:
#             factors.append(i)
#         break
# # print(factors)
#
# # 소수 꺼내기
# cnt = 0
# result = []
# for factor in factors:
#     for i in range(2, factor):
#         if factor % i == 0:
#             cnt += 1
#             break  # break로 for문을 끝내줘야 시간초과가 뜨지 않음
#     if cnt == 0:
#         result.append(factor)
# # print(result)
#
# 1이 될때까지 소수로 나눠서 정렬 후 출력
# nums = []
# while N != 1:
#     for i in result:
#         if N % i == 0:
#             nums.append(i)
#             N = N // i
# print(*sorted(nums), sep='\n')
