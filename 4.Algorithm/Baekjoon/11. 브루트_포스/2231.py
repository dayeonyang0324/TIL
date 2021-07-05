# 2331

N = int(input())
result = 0
for i in range(1, N+1):
    num = list(map(int, str(i)))  # 숫자 각 자리들의 리스트
    result = i + sum(num)  # 숫자 각 자리의 합과 해당 숫자를 더한다
    if result == N:
        print(i)
        break

    if i == N:  # 생성자가 없으면 0을 출력
        print(0)
