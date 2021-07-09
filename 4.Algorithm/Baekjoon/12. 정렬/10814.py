# 10814

N = int(input())
people = []
for i in range(N):
    # str, int를 설정하지 않고 구했더니 output은 잘 나오지만 틀렸다고 함
    age, name = map(str, input().split())
    age = int(age)
    people.append([age, i, name])  # 나이 다음 등록 순서를 위해 i값을 넣었다

# append 값에 i 삭제후 람다를 사용해도 된다.
# people.sort(key=lambda x: x[0])
people.sort()

for i in range(N):
    print(people[i][0], people[i][2])
