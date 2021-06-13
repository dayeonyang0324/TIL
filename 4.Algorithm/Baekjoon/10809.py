# 10809

# 단어를 받아오고
word = input()
# 값을 비교하기 위한 알파벳 목록을 준다
alpha = ['a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 체크하기 위한 리스트를 만들고 편하게 -1로 초기화한다
check = [-1 for _ in range(26)]

# 알파벳을 하나씩 돌면서 단어에 들어있다면 check 리스트를 갱신한다
for i in range(len(alpha)):
    if alpha[i] in word:
        check[i] = word.find(alpha[i])

# 리스트 출력이 아닌 요소만 출력!!
for j in check:
    print(j, end=' ')
