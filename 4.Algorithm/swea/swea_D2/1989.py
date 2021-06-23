
T = int(input())
for tc in range(1, T+1):
    word = list(input())
    print('#{}'.format(tc), end=' ')

    if word[::-1] == word:  # 단어 뒤에서부터 검색해서 현재 단어와 같다면
        print(1)  # 1 출력
    else:
        print(0)  # 아니라면 0 출력


