# 인덱스를 1부터 주기 위해 [0]을 추가함
num = [0] + list(int(input()) for _ in range(9))

# 리스트의 최댓값과 인덱스는 내장함수 사용
print(max(num))
print(num.index(max(num)))