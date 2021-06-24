# 1085

x, y, w, h = map(int, input().split())
# x가 갈 수 있는 거리, y가 갈 수 있는 거리
result = [abs(w-x), x, abs(h-y), y]
# 그 중 최소값
print(min(result))
