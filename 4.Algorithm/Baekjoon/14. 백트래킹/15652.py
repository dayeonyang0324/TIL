# 15652

N, M = map(int, input().split())
result = []


# 중복없이 담아야 하므로 j변수 추가
def back(j):
    if len(result) == M:
        print(*result)
        return

    # j부터 돌기 시작하지만
    for i in range(j, N + 1):
        result.append(i)
        # 중복된 수도 가능하므로 값은 그대로 넣기
        back(i)
        result.pop()


back(1)
