import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')


def bruteforce(word, sentence):
    N = len(word)
    M = len(sentence)
    result = 0

    for i in range(M - N + 1):  # 문장의 길이에서 단어를 뺀 횟수만큼 회문을 돈다
        cnt = 0
        for j in range(N):
            if sentence[i + j] == word[j]:  # 단어의 첫 단어가 문장에 있으면 확인하고 단어의 다음 요소까지 확인한다.
                cnt += 1  # 맞은 갯수만큼 cnt증가
            else:
                break

        if cnt == N:  # cnt가 단어 길이만큼 있으면 같다는 뜻이므로 결과값 1 증가
            result += 1

    return result


T = 10
for tc in range(1, T+1):
    n = int(input())
    word = list(input())
    sentence = list(input())

    print('#{} {}'.format(tc, bruteforce(word, sentence)))


#####################################################

# 부르트포스트로 풀 수 있지만 tttt에서 tt를 찾으면 3이 나온다. 여기서는 오류가 나진 않지만 다르게 풀어봤다.
T = 10
for tc in range(1, T+1):
    n = int(input())
    word = list(input())
    sentence = list(input())

    i = 0
    ans = 0
    while i < len(sentence) - len(word) + 1:
        if sentence[i:i+len(word)] == word:  # 단어의 길이만큼 문장에서 슬라이싱하고
            i += len(word)  # 슬라이싱 만큼은 확인하지 않고 넘어가야 하니 단어 길이만큼 넘어간다.
            ans += 1
        else:
            i += 1  # 만족하지 않다면 바로 옆으로 이동한다.

    print('#{} {}'.format(tc, ans))