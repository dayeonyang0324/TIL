# 2580

import sys
table = [list(map(int, input().split())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if table[i][j] == 0]


def check(i, j):
    nums = [i+1 for i in range(9)]

    # 행, 열에 숫자가 있는지 확인하기 - 있는 수들은 제거해서 목록 남겨놓기
    for k in range(9):
        if table[i][k] in nums:
            nums.remove(table[i][k])
        if table[k][j] in nums:
            nums.remove(table[k][j])

    # 작은 격자에 수가 있는지 확인해서 목록 남겨놓기
    for s in range((i // 3)*3, ((i // 3)+1)*3):
        for b in range((j // 3)*3, ((j // 3)+1)*3):
            if table[s][b] in nums:
                nums.remove(table[s][b])

    return nums


# Python은 시간초과 Pypy3는 return하면 틀림 -> sys.exit() 써줘서 강제 종료하기
def sdoku(index):
    if index == len(zero):
        for i in table:
            print(*i)
        sys.exit()

    (i, j) = zero[index]
    for num in check(i, j):
        table[i][j] = num
        sdoku(index + 1)
        table[i][j] = 0


sdoku(0)


# 실패 코드
# def row(i, j):
#     row = [0] * 10
#     for r in range(9):
#         row[table[i][r]] += 1
#
#     for r in range(1, 10):
#         if row[r] == 1:
#             pass
#         return row.index(row[r])
#
#
# def col(i, j):
#     col = [0] * 10
#     for c in range(9):
#         col[table[c][j]] += 1
#
#     for c in range(1, 10):
#         if col[c] == 1:
#             pass
#         return col.index(col[c])
#
#
# def smallbox(i, j):
#     small = [0] * 10
#     for s in range(3*(i // 3), 3*((i // 3) + 1)):
#         for b in range(3*(i // 3), 3*((i // 3) + 1)):
#             small[table[s][b]] += 1
#
#     for s in range(1, 10):
#         if small[s] == 1:
#             pass
#         return small.index(small[s])
#
#
# def sdoku(index):
#     if index == len(zero):
#         for i in table:
#             print(*i)
#         return
#
#     (i, j) = zero[index]
#     for k in range(1, 10):
#         if row(i, j) == col(i, j) == smallbox(i, j):
#             table[i][j] = k
#             print(table[i][j])
#             sdoku(index + 1)
#             table[i][j] = 0
#
#
# table = [list(map(int, input().split())) for _ in range(9)]
# zero = [(i, j) for i in range(9) for j in range(9) if table[i][j] == 0]
# sdoku(0)
