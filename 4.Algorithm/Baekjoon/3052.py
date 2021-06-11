# 3052

num = list(int(input()) for _ in range(10))
# 나머지 담을 빈 리스트
result = []
for i in num:
    # 나머지가 결과에 담겨있지 않을때만 append
    if i % 42 not in result:
        result.append(i % 42)
# 결과의 전체 길이 출력
print(len(result))