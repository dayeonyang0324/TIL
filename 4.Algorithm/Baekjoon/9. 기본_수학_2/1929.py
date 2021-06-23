# 1929

def prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


M, N = map(int, input().split())

for num in range(M, N+1):
    if prime(num):
        print(num)


# 2581 방식에 제곱근을 사용했는데 틀렸다.. 왜 틀렸는지 모르겠다..
# M, N = map(int, input().split())
# for num in range(M, N+1):
#     cnt = 0
#     if M > 1:
#         # 2581 문제와 유사하지만 시간초과
#         # 소수를 찾기 위해서 제곱근까지만 확인
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 cnt += 1
#                 break
#         if cnt == 0:
#             print(num)
