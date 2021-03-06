# 두 개의 문자열을 비교할때,
# A의 첫번째 요소가 B전체에 있는지 다 확인한다
# 그 다음은 A의 두번째 요소가 B전체에 있는지 다 확인한다.
# 이런 방식을 계속 반복해나간다.


p = 'is'  # 찾으려는 패턴
t = 'this is my world'

M = len(p)
N = len(t)


def Bruteforce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i -= j
            j = -1
        i = j + 1
        j = j + 1
    if j == M:
        return i - M
    else:
        return -1


print(Bruteforce(p, t))


# for문
def Bruteforce2(p, t):
    N = len(t)
    M = len(p)

    for i in range(N - M + 1):
        cnt = 0
        for j in range(M):
            if t[i + j] == p[j]:
                cnt += 1
            else:
                break

        if cnt == M:
            return 1

    return -1


print(Bruteforce2(p, t))
