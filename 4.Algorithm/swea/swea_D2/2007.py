
T = int(input())
for tc in range(1, T+1):
    word = list(input())

    madi = []  # 마디를 구할 리스트 생성
    for i in range(len(word)):
        if word[0: i] == word[i: 2*i]:  # for문을 돌면서 0부터 i까지가 i부터 2i와 같다면
            madi.append(word[0:i])  # 같은 부분이 마디이므로 리스트에 추가
    print('#{} {}'.format(tc, len(madi[1])))  # 리스트 요소 1번째가 가장 짧은 마디이므로 출력
