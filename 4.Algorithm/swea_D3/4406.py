
T = int(input())
for tc in range(1, T+1):
    word = list(input())

    result = []
    aeiou = ['a', 'e', 'i', 'o', 'u']  # 모음 리스트를 만들어 준다
    for i in range(len(word)):
        if word[i] in aeiou:  # 만약에 모음 안에 있으면 그냥 지나감
            continue
        result.append(word[i])  # 나머지는 새로운 리스트에 넣어줌
    print('#{} {}'.format(tc, ''.join(result)))
