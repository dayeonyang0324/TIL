# 4673

# 생성자를 구하는 함수 만들기
def num(a):
    ans = int(a)
    # 문자열로 만들어 for문을 돌리고 int로 만들어 값을 더해줌
    for i in str(a):
        ans += int(i)
    return ans


# 생성자들을 위한 리스트 만들기
generated_list = []
for i in range(1, 10001):
    generated_list.append(num(i))

# 10000까지의 수 중에 생성자가 없으면 출력하기
for j in range(1, 10001):
    if j not in generated_list:
        print(j)
