# 1002

T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 원의 접접의 갯수 구하기
    # 중심 거리
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 중심 거리가 0이고 반지름이 같다면 원 위의 모든 점이 가능 = 무한대
    if d == 0:
        if r1 == r2:
            print(-1)
        # 아니라면 접접이 없음
        else:
            print(0)
    else:
        # 반지름 보다 거리가 더 크면 접점 없음
        if d > (r1 + r2) or d < abs(r1 - r2):
            print(0)
        # 두 원이 한 점에서 접할 때
        elif d == (r1 + r2) or d == abs(r1 - r2):
            print(1)
        # 두 원이 두 접점에서 만날 때
        else:
            print(2)
