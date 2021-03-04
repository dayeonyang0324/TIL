import sys
sys.stdin = open('input.txt')


def row(num):
    # 가로
    for i in range(9):
        check = [0 for _ in range(9)]  # 1부터 9까지 셀 수 있는 리스트 만들기
        for j in range(9):
            check[num[i][j]-1] += 1  # 가로줄을 하나씩 돌면서 해당하는 인덱스에 1을 추가
        for k in range(9):
            if check[k] != 1:  # 모든 요소에 1이 있다면 1~9 만족, 1이 아닌 다른 수가 있다면 False
                return False
    return True


def col(num):
    # 세로
    for j in range(9):
        check = [0 for _ in range(9)]
        for i in range(9):
            check[num[i][j] - 1] += 1
        for k in range(9):
            if check[k] != 1:
                return False
    return True


def hol(num):
    # 작은 격자
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):  # 3칸 * 3칸을 검사할 수 있도록 for문을 만들어 줌.
            check = [0 for _ in range(9)]
            for k in range(3):
                for t in range(3):
                    check[num[i+k][j+t]-1] += 1
            for l in range(9):
                if check[l] != 1:
                    return False
    return True


T = int(input())
for tc in range(1, T+1):
    num = [list(map(int, input().split())) for _ in range(9)]
    # 가로, 세로, 작은 격자 모두 만족할때 반환값은 True이므로 1, 아니라면 반환값은 0
    print('#{} {}'.format(tc, int(row(num) and col(num) and hol(num))))
