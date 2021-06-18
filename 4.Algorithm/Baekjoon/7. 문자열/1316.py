# 1316
# 처음 문제를 접하고 check 리스트를 만들고 while 문을 돌릴려고 했었다.
# for 문을 사용해서 해당 단어가 연속되지 않은 상태 + 해당 단어 이후 슬라이싱 한 새로운 단어에서
# 나타나지 않는다는 조건으로 코드를 짜면 되는 간단한 문제였지만 전혀 생각하지 못했다..

N = int(input())

cnt = 0
# 단어 목록을 순회하면서 input 받기
for _ in range(N):
    word = input()
    cnt += 1
    # 개별 단어의 요소를 순회하면서
    for i in range(len(word)-1):
        # 단어가 연속이지 않을때
        if word[i] != word[i+1]:
            # 해당 단어를 제외한 나머지 단어에 해당 단어가 나타난다면
            if word[i] in word[i+1:]:
                # 실패한 단어 갯수를 빼주고 break
                cnt -= 1
                break

print(cnt)
