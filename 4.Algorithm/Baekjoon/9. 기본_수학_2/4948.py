# 4948

# 1929 문제와 유사하게 풀었지만 시간초과
def prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    N = int(input())
    cnt = 0
    for num in range(N+1, 2*N + 1):
        if prime(num):
            cnt += 1
    if N == 0:
        break
    print(cnt)

# 베르트랑 공준
# 체크하기 위한 리스트 만들어서 제곱근들을 확인하기
N = 123456 * 2 + 1
check = [True] * N
for i in range(2, int(N**0.5)+1):
    if check[i]:
        for j in range(2*i, N, i):
            check[j] = False


# 기존의 방법과 유사하게 탐색 후 갯수 세기
def prime(N):
    cnt = 0
    for i in range(N + 1, N * 2 + 1):
        if check[i]:
            cnt += 1
    print(cnt)


while True:
    N = int(input())
    if N == 0:
        break
    prime(N)
