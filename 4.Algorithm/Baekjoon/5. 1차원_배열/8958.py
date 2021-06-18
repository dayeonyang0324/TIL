# 8958
T = int(input())
for tc in range(1, T+1):
    quiz = input()

    # 총점, 연속으로 O이 나올때 count 할 변수
    score = 0
    cnt = 0
    for i in range(len(quiz)):
        # O이 나온다면 갯수 증가, 점수에 합산
        if quiz[i] == 'O':
            cnt += 1
            score += cnt
        # X가 나온다면 개수는 0으로 초기화
        elif quiz[i] == 'X':
            cnt = 0
    print(score)
