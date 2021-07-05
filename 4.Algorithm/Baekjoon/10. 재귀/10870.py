# 10870

N = int(input())


# 피보나치 수열 함수
# 0일때 0, 1일때 1로 초기값 2개 주기
def fivo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fivo(N-1) + fivo(N-2)


# 결과값 출력
print(fivo(N))
