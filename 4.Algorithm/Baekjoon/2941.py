# 2941

word = input()
# 크로아티아 문자들 바꾸기
alpha = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

# 인덱스로 접근하기 위해 while문 사용
i = 0
cnt = 0
while i < len(word):
    # 2개 슬라이싱해서 값이 있으면 인덱스와 문자 수 증가
    if word[i:i+2] in alpha:
        cnt += 1
        i += 2
    # 유일한 3자리라서 따로 분기
    elif word[i:i+3] == 'dz=':
        i += 3
        cnt += 1
    # 그 외 문자들도 인덱스와 문자 수 증가
    else:
        i += 1
        cnt += 1
print(cnt)
