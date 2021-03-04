import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    table = [list(input()) for _ in range(5)]

    # 제일 긴 문자열만큼 순회하기 위해 긴 길이 구하기
    maxi = 0
    for k in table:
        if len(k) > maxi:
            maxi = len(k)

    # 하나씩 순회하면서 부족한 부분은 기호로 채우기
    for i in range(len(table)):
        if len(table[i]) < maxi:
            for j in range(maxi - len(table[i])):
                table[i].append('*')

    result = ''
    for i in range(maxi):
        for j in range(5):
            if table[j][i] == '*':
                continue  # 만약 기호가 들어있으면 그건 빼고 결과값에 저장하기
            result += table[j][i]

    print('#{} {}'.format(tc, result))


###################################################

# 다른 풀이 #
T = int(input())
for tc in range(1, T+1):
    word = [0] * 5
    max_len = 0

    for i in range(5):
        word[i] = list(input())

        if len(word[i]) > max_len:
            max_len = len(word)

    print('#{}'.format(tc), end='')
    for i in range(max_len):
        for j in range(5):
            # if len(word[j]) > i:
            #     print(word[j][i], end='')
            try:
                print(word[j][i], end='')
            except:
                pass
    print()