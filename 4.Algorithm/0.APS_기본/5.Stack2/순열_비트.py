arr = [1, 2, 3]
N = 3
sel = [0] * N  # 뽑은 결과

def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        # j번째 원소 활용했으면 사용하면 안됨
        if check & (1 << j):
            continue

        sel[idx] = arr[j]
        perm(idx+1, check | (1 << j))  #원상복구 필요없다


perm(0, 0)