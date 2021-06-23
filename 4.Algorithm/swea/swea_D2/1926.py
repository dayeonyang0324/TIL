
N = int(input())
num = ['3', '6', '9']  # 있는지 확인해야 하는 숫자들
for i in range(1, N+1):
    cnt = 0
    for j in str(i):  # 십의자리와 일의자리를 따로 비교하기 위해서는 str로 만들고 한자리씩 비교
        if j in num:
            cnt += 1  # 들어있는만큼 갯수 세기
    if cnt > 0:
        i = cnt * '-'  # 갯수만큼 '-' 넣어서 출력하기

    print(i, end=' ')