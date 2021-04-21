def factiroal(n):
    if n == 1:  # 1일때까지 반복
        return 1
    return n * factiroal(n - 1)  # 재귀 표현 방식


print(factiroal(5))
