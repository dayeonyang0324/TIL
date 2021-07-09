# 1181

N = int(input())
# 중복없이 단어의 길이별로 리스트에 넣어 sort 했다
words = []
cnt = []
for _ in range(N):
    word = input()
    # 중복없이 넣기 위해 if 문을 넣었지만 정렬이 되지않아
    # 값이 나왔는지 체크하기 위해 cnt 리스트를 만들었다
    if word not in cnt:
        words.append([len(word), word])
        cnt.append(word)
words.sort()

# 단어 길이별로, 알파벳 순서로 정렬되어 그대로 출력한다
for i in range(len(words)):
    print(words[i][1])


########################################
# 람다를 사용해 정렬할 수도 있다 (숫자, 알파벳)
words.sort(key = lambda word: (words[0], words[1]))
# sort에 key값을 넣어 정렬할 수도 있다
words.sort(key = len)
