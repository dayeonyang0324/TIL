# 1546

N = int(input())
# 점수 리스트로 받기
score = list(map(int, input().split()))
# 최대 점수 출력
max_score = max(score)

# 조작한 점수 리스트로 만들기
new_score = []
for i in score:
    new_score.append(i / max_score * 100)

# 조작된 점수의 평균 구하기(sum함수 사용해버림..)
# total = 0
# for i in new_score:
#     total += i
# print(total/N)

print(sum(new_score)/N)
