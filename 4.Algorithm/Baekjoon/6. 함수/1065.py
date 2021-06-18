# 1065

# 한수를 찾기 위한 함수 만들기
def one_num(N):
    cnt = 0
    # 범위의 수 만큼 for문 돌기
    for i in range(1, N+1):
        # 99까지는 모두 조건 만족
        # 각각의 자리수가 일정하게 증가하면 됨
        if i < 100:
            cnt += 1
        # 조건은 999까지 확인하면 되는데 3자리 수 중 236이런 경우 한수가 아님, 123은 한수이다
        else:
            num = list(map(int, str(i)))  # 리스트로 변환해서
            if num[0] - num[1] == num[1] - num[2]:  # 각 자리수가 증차수열인지 확인
                cnt += 1
    return cnt


N = int(input())
print(one_num(N))
