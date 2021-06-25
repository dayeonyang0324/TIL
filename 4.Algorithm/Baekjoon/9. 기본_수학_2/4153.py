# 4153

while True:
    tri = list(map(int, input().split()))
    # 출력을 받아서 모든 요소가 0이라면 break
    if tri[0] == tri[1] == tri[2] == 0:
        break

    # 피타고라스 정리에 의해 제일 큰 변의 제곱이 나머지 제곱의 합과 같아야 한다
    long = max(tri)
    tri.remove(max(tri))  # 큰 변의 길이를 제외한 나머지 길이
    # 피타고라스 정리 만족 유무
    if long ** 2 == tri[0] ** 2 + tri[1] ** 2:
        print('right')
    else:
        print('wrong')

