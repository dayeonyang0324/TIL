# 10872

N = int(input())


# 팩토리얼 계산 함수
def facto(N):
    if N == 0:
        return 1
    else:
        return N * facto(N - 1)


# 결과값
print(facto(N))
