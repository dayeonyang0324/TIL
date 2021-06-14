# 1157

# 문자열에서 가장 까다로웠던 문제.. 딕셔너리로 만드니깐 더 복잡한 듯 하다..

# 대문자로 출력해야하므로 입력값을 다 대문자로 변환 upper 사용
word = input().upper()

# 단어 딕셔너리 만들기
result = {}
for i in word:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1


# 최대 value 값으로 key 찾기 위한 함수 생성..
def get_key(v):
    for key, value in result.items():
        if v == value:
            return key


# 최대 value 구하기
values = list(result.values())
# 함수 대신 key 값들의 리스트에서 찾기
# keys = list(result.keys())

# 최대 value 를 count 해서 길이가 1이 넘는다면 ? 출력
if values.count(max(values)) > 1:
    print('?')
# 아니라면 최대 value를 가진 key 찾기
else:
    print(get_key(max(values)))
    # 최대 value에 해당하는 인덱스를 찾아 key 값 찾기
    # print(keys[values.index(max(values))])
