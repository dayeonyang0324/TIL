def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibo(10))

################################

# memoization : 계산값을 줄일 수 있음
# 값들을 메모해서 반복계산하지 않고 계속 사용할 수 있음


def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]


memo = [0, 1]
print(fibo1(40))


##################################
memo2 = [-1]*21
memo2[0] = 0
memo2[1] = 1


def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

print(fibo2(10))
print(memo2)