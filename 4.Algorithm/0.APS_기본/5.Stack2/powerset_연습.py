# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합
N = 10
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [0] * N


def solution(idx):
    if idx == N:
        if sum(check) == 10:
            print(check)
        return
    check[idx] = 0
    solution(idx + 1)

    check[idx] = idx+1
    solution(idx + 1)


solution(0)


########################################################


data = list(range(1, 11))
is_selected = [None] * len(data)
result = []


def power_set(idx):
    # is_selected 를 다 채우지 못했다면
    if idx < len(data):
        is_selected[idx] = True
        power_set(idx+1)
        is_selected[idx] = False
        power_set(idx+1)
    # 다 채웠다면 (idx == len(data))
    else:
        total = 0
        for i in range(len(data)):
            if is_selected[i]:
                total += data[i]
            if total == 10:
                result.append(is_selected[:])
            return None  # 함수 끝


power_set(0)