# 1712

A, B, C = map(int, input().split())

# 판매 비용 C 가 가변 비용 B 보다 커야함
if B >= C:
    print(-1)
else:
    # 필요한 수량을 계산으로 구할 수 있음
    print(A//(C-B) + 1)
    # while 문 사용하려 했으나 21억 까지 계산하는데 너무 오래걸림
    # while A + B * cnt >= C * cnt:
    #     cnt += 1
    #     if A + B * cnt < C * cnt:
    #         result = cnt
    #         break
