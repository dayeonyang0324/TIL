numbers = [2, 6, 1, 3, 9]


def merge_sort(numbers):
    N = len(numbers)
    # base case => numbers의 길이가 2보다 작다면 (0, 1) 그대로 리턴
    if N < 2:
        return numbers

    # 중간점 찾기
    mid_idx = N // 2
    # 중간점 기준 왼쪽 리스트
    left = numbers[:mid_idx]
    # 중간점 기준 오른쪽 리스트
    right = numbers[mid_idx:]

    # 정렬된 왼쪽
    sorted_left = merge_sort(left)
    # 정렬된 오른쪽
    sorted_right = merge_sort(right)

    # 최종 병합된 결과
    merged = []
    l = r = 0
    while l < len(sorted_left) and r < len(sorted_right):
        # 좌우 맨 앞에서 더 작은 값을 최종 결과에 추가
        if sorted_left[l] < sorted_right[r]:
            merged.append(sorted_left[l])
            l += 1
        else:
            merged.append(sorted_right[r])
            r += 1

    # 좌우 남은 숫자들은 이미 정렬되어 있으므로 그대로 병합
    # 1.
    # while l < len(sorted_left):
    #     merged.append(sorted_left[l])
    #     l += 1
    # while r < len(sorted_right):
    #     merged.append(sorted_right[r])
    #     r += 1

    # 2.
    merged += sorted_left[l:]
    merged += sorted_right[r:]

    return merged


print(merge_sort(numbers))