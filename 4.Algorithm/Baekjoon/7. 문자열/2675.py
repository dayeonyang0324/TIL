# 2675

T = int(input())
for tc in range(1, T + 1):
    input_item = list(map(str, input().split()))
    N = int(input_item[0])
    word = input_item[1]

    # 결과값 str 로 저장
    result = ''
    # 단어 길이만큼 for 문
    for i in range(len(word)):
        # 단어 당 N번 반복
        for j in range(N):
            result += word[i]
    print(result)
