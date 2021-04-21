# 중앙 값을 기준으로 중앙의 왼쪽에 있는지 오른쪽에 있는지 판단한다
# APS_기본 > 5.Stack2 > 퀵정렬.py
# 5207 이진 탐색 문제


def binary_search(a, b):
    global cnt

    for key in b:
        start = 0
        end = len(a) - 1
        flag = 0
        while start <= end:
            # 판단하기 위한 중앙 값 설정
            middle = (start + end)//2

            if key == a[middle]:
                cnt += 1
                break

            elif key < a[middle]:
                end = middle - 1
                # 왼쪽 오른쪽 번갈아가면서 진행해야하므로 체크하기 위한 flag값 설정
                if flag == 1:
                    break
                flag = 1

            else:
                start = middle + 1
                if flag == -1:
                    break
                flag = -1