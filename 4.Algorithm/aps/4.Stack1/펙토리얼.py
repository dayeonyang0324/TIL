def factiroal(n):
    if n == 1:
        return 1
    return n * factiroal(n - 1)

print(factiroal(5))
