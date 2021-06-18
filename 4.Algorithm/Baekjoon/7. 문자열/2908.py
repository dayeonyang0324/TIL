# 2908

nums = list(input().split())

result = []
# 리스트 안의 각각의 숫자들(chr)의 순서를 뒤집기 위해 for 문 사용
for num in nums:
    # 새로 바뀐 숫자들을 문자열로 받기
    change_num = ''
    for j in range(len(num)-1, -1, -1):
        change_num += num[j]
    # 문자열로 받은 수들을 리스트에 int로 append
    result.append(int(change_num))

# maxi = 0
# for i in result:
#     if i > maxi:
#         maxi = i
# print(maxi)

# 새로 바뀐 리스트에서 최댓값 구하기 max 사용
print(max(result))
