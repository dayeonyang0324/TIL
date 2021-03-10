
# 해당 문제는 파이썬을 지원하지 않음..

T = int(input())
for tc in range(1, T+1):
    letter = list(input().split())
    print('#{}'.format(tc), end=' ')

    # 구멍이 1개와 2개인 단어들의 리스트를 만든다
    blank1 = ['A', 'D', 'O', 'P', 'Q', 'R']
    blank2 = ['B']

    # 처음에 나오는 단어
    word1 = 0
    word11 = 0

    # 순회를 돌면서 구멍이 1개인 단어와 2개인 단어의 갯수를 구한다
    for word in letter[0]:
        if word in blank1:
            word1 += 1
        if word in blank2:
            word11 += 1

    # 두번째 단어
    word2 = 0
    word22 = 0
    # 순회를 돌면서 구멍이 1개인 단어와 2개인 단어의 갯수를 구한다
    for word in letter[1]:
        if word in blank1:
            word2 += 1
        if word in blank2:
            word22 += 1

    # 두 단어의 구멍이 1개인 갯수와 2개인 갯수가 같다면 같은 문자로 판별한다
    if word1 == word2 and word11 == word22:
        print('SAME')
    else:  # 하나라도 다르다면 다른 단어이다
        print('DIFF')