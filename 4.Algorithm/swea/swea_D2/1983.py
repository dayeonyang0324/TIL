T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(n)]

    # 총점을 계산하는 과정
    total = [[] for _ in range(n)]
    for i in range(n):
        sum_score = (score[i][0] * 0.35) + (score[i][1] * 0.45) + (score[i][2] * 0.2)
        total[i].append([sum_score, i+1])  # 총점이랑 몇번쨰 학생인지 같이 리스트에 추가

    total.sort()
    total.reverse()  # 점수를 내림차순으로 정렬 (점수로만 정렬, 학생 숫자는 그냥 따라옴)

    # 학생 번호가 k와 같으면 몇 등인지 인덱스로 파악함
    now = 0
    for i in range(len(total)):
        if total[i][0][1] == k:
            now = i

    # 학생 수는 10명 단위이므로 50명이면 5등 단위로 학점이 바뀐다.
    abc = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    # 찾고자 하는 학생을 단위로 나눠주고 인덱스 처리해주면 학점을 알 수 있다.
    print('#{} {}'.format(tc, abc[now//(n//10)]))




