# 2869

A, B, V = map(int, input().split())

# 시간 초과
# cnt = 0
# while (A-B) * cnt < V:
#     cnt += 1
# print(cnt)

cnt = 0
# 올라가야 할 높이 V-B : 정상에 도착하면 내려가지 않으므로
# 나눠떨어지면 낮, 밤 모두 필요하단것
if (V-B) % (A-B) == 0:
    cnt = (V-B) // (A-B)
# 하루가 지나고 한번 더 올라가야 정상 도착
else:
    cnt = (V-B) // (A-B) + 1
print(cnt)
