
N = int(input())
result = 0
for i in range(1, N+1):
    num = list(map(int, str(i)))  # 숫자들의 각자리 수의 합과 전체 숫자의 합이 필요하다
    result = i + sum(num)
    if result == N:
        print(i)
        break

    if i == N:  # 생성자가 없으면 0을 출력
        print(0)
