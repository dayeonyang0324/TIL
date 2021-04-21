
# 부분집합을 for문을 사용해서 하나하나 구하는거 = 매우 매우 길어짐 주의
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(*bit)


# & 이진수끼리의 and값을 반환 : 0010과 0110을 비교해서 0010 반환
print(2 & 6)

# | 이진수끼리의 or값을 반환 : 0010과 0110을 비교해서 0110 반환
print(2 | 6)


# 1 << n : 1을 n만큼 이동한다는 의미, 원소가 n개 일떄의 모든 부분집합의 수
# i & (1 << j) : i의 j번째 비트가 1인지 아닌지 리턴한다.
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            # 이런식으로 프린트를 하면 부분집합 안의 요소 하나하나를 뜻한다.(1 / 1 2 / 1 2 3)
            # 리스트로 묶으고 싶으면 전체 리스트와 중간 리스트를 만들어서 넣고 넣어야한다.
            print(arr[j], end = ',')
            # 중간리스트.append(arr[j])
    print()
    # 전체리스트.append(중간리스트)
print()


