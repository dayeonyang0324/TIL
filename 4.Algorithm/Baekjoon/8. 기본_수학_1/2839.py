# 2839

N = int(input())

# 5i + 3j = N
# i + j = ?

result = 0
# 한 종류일때 최대 가능한 봉지 갯수는 몫
for i in range(N//5 + 1):
    for j in range(N//3 + 1):
        # 각자 최대 가능한 몫만큼 for 문 돌면서 if 조건
        if 5 * i + 3 * j == N:
            # print(i, j)  가능한 모든 경우들
            result = i + j
# 값이 없으면 -1이 출력
if result == 0:
    result = -1
print(result)
