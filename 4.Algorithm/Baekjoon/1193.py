# 1193

# 숫자를 받고
num = int(input())

# total 은 수열을 나타내며 이를 통해 1, 3, 6, 10 ... 에서 어디에 위치한지 알 수 있다
# i는 total 에 해당하는 수열의 인덱스를 나타낸다
total = 1
i = 0
while total < num:
    i += 1
    total += i + 1

# check 는 분수 각 자리의 합이 i보다 1 큰수 이므로 지정해놓는다
check = i + 1
# 합이 홀수이면 대각선 위로 올라가고 짝수면 대각선 아래로 내려간다
if check % 2 == 1:
    print('{}/{}'.format(total - num + 1, check + 1 - (total - num + 1)))
else:
    print('{}/{}'.format(check + 1 - (total - num + 1), total - num + 1))
