# 4344
T = int(input())
for _ in range(1, T+1):
    num = list(map(int, input().split()))
    N = num[0] # 학생 수
    student = [num[i] for i in range(1, len(num))] # 학생 점수

    avg = sum(student)/N  # 학생 점수 평균(내장함수 사용)
    cnt = 0  # 평균 이상 학생 count
    for i in student:
        if i > avg:
            cnt += 1
    # 소숫점 3자리까지 백분율로 나타내는 %사용
    print('%.3f%%' %(cnt/N * 100))
