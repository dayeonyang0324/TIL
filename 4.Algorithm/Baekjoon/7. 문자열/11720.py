# 11720

N = int(input())
# N은 중요하지 않아보임.. 숫자를 리스트로 받아와서 각각의 요소를 더하기
num = list(map(int, input()))
total = 0
for i in num:
    total += i
print(total)

N = int(input())
num = list(map(int, input()))
# 숫자들이 리스트로 들어와있어서 내장함수 sum을 사용해도 됨
print(sum(num))