# 숫자들 배열 중에서 1개씩만 바꿔서 10진법으로 변환 후 리스트에 담기
# 2진수에서 0 -> 1, 1 -> 0으로 바꾸는 함수
def change_two(two):
    global answer_two
    two_result = []
    i = 0
    while i < len(two):
        two_list = list(two)
        if two_list[i] == '1':
            two_list[i] = '0'
            two_result.append(''.join(two_list))
        else:
            two_list[i] = '1'
            two_result.append(''.join(two_list))

        i += 1

    answer_two = []
    for i in two_result:
        answer_two.append(int(i, 2))

    return answer_two


# 3진수의 숫자를 하나씩 바꾼 모든 수들의 리스트를 10진법으로 바꾼 후 최종 리스트 만들기
def change_three(three):
    global answer_three
    three_result = []
    i = 0
    while i < len(three):
        three_list = list(three)
        if three_list[i] == '2':
            three_list[i] = '1'
            three_result.append(''.join(three_list))
            three_list[i] = '0'
            three_result.append(''.join(three_list))

        elif three_list[i] == '1':
            three_list[i] = '2'
            three_result.append(''.join(three_list))
            three_list[i] = '0'
            three_result.append(''.join(three_list))
        else:
            three_list[i] = '2'
            three_result.append(''.join(three_list))
            three_list[i] = '1'
            three_result.append(''.join(three_list))

        i += 1

    for i in three_result:
        answer_three.append(int(i, 3))

    return answer_three


T = int(input())
for tc in range(1, T + 1):
    two = input()
    three = input()

    # 이진수를 10진법으로, 3진수를 10진법으로 나타내는 방법
    # answer_two = int(two, 2)
    # answer_three = int(three, 3)

    answer_two = []
    answer_three = []

    change_two(two)
    change_three(three)

    # 2진수를 10진수로 만든 최종 리스트와 3진수를 10진수로 만든 최종 리스트 비교
    for i in range(len(answer_two)):
        if answer_two[i] in answer_three:
            print('#{} {}'.format(tc, answer_two[i]))