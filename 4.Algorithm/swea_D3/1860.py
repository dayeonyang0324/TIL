import sys
sys.stdin = open('input.txt')

# 사람들이 오는 시간(초)을 오름차순으로 정렬하는 함수 생성 : bubble_sort활용
def sort(time):
    for j in range(len(time)-1, 0, -1):
        for i in range(j):
            if time[i] > time[i+1]:
                time[i], time[i+1] = time[i+1], time[i]
    return time


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # N 사람, M 걸리는 시간, K 붕어빵 개수
    time = sort(list(map(int, input().split())))

    table = [0] * (time[-1]+1)  # 제일 늦게오는 사람 기준 sec나열, 사람이 오는 시간은 table 의 인덱스 (3초에 오면 table[3])
    total = 0  # 초 당 붕어빵의 갯수
    for i in range(1, len(table)):
        if i % M == 0:  # 2초당 2개면 2초에는 2개, 3초에도 2개, 4초에는 4개
            total += K  # 걸리는 시간에 붕어빵 갯수 더해서 누적
        table[i] += total  # 누적된 붕어빵을 table 요소에 더해줌

    for t in time:
        for m in range(t, len(table)):  # t초에 오는 사람이 1개 먹으면 그 뒤로는 누적 붕어빵이 1만큼 감소
            table[m] -= 1  # 2초 2개, 3초 2개, 4초 4개 -> (3초에 사람이 오면) 3초 1개, 4초 3개 ...

    result = 'Possible'
    for f in range(len(table)):
        if table[f] < 0:  # 과정을 다 끝낸 후 붕어빵의 갯수에 음수 값이 존재한다면 실패!
            result = 'Impossible'
            break  # 한개라도 존재하면 바로 멈추고 'Impossible'출력함. 기본값은 'Possible'

    print('#{} {}'.format(tc, result))


############################################3
# 다른 사람 풀이

# def solution():
#     cnt = 0
#     # 11,111이하로 조건
#     for idx in range(11112):
#         if idx % M == 0 and idx != 0:
#             cnt += K
#
#         while idx == people[0]:
#             if cnt == 0:
#                 return 'Impossible'
#             else:
#                 cnt -= 1
#                 people.pop(0)
#
#             if len(people) == 0:
#                 return 'Possible'
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     people = sorted(list(map(int, input().split())))
#
#     print('#{} {}'.format(tc, solution()))
