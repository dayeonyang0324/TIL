
# 카운팅 정렬은 정수에만 적용 가능하다.
# list에서 (가장 큰 값 + 1) 크기의 count리스트를 만든다.
# count = [0] * (N)


def counting(arr, N):
    count_arr = [0] * (N+1)  # 빈도 수를 셀 리스트 만들기

    # 빈도수 세기
    for i in arr:
        count_arr[i] += 1

    # 직전값 누적시켜 빈도수 업데이트
    for i in range(N):
        count_arr[i+1] += count_arr[i]

    # 결과 초기값 리스트
    result = [-1] * len(arr)

    # 역순으로 순회를 돌면서 결과값을 채워넣고 빈도수를 감소시킨다
    for i in arr:
        result[count_arr[i] - 1] = i
        count_arr[i] -= 1

    return result