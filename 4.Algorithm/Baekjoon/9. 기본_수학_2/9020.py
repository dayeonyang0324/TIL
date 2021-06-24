# 9020

# 시간초과
# def prime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     result = []
#     for i in range(1, N//2 + 1):
#         if prime(i) and prime(N-i):
#             result.append([i, N-i])
#     print(*result[-1])


# 기존 소수 문제들과 똑같이 소수를 구하는 함수를 만들었다
def prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


T = int(input())
for tc in range(T):
    N = int(input())
    result = []
    # 절반만 확인하면 뒤에는 반복하기 때문에 반만 확인했다 (내림차순으로 확인)
    for i in range(N//2, 1, -1):
        if prime(N-i) and prime(i):
            # 바로 출력하고 값이 나온다면 break를 하니 시간초과가 나지 않았다
            print(i, N-i)
            break
