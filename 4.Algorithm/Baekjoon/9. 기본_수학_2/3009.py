# 3009

# 주어진 좌표들을 정리
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# x 좌표에서 같은 값이 2개, 1개 주어졌을 때 1개만 있는 값이 최종값이 되어야한다
# 리스트에 넣으면서 값이 있으면 빼면 최종적으로 남는 1개가 답이 된다
x = [x1, x2, x3]
result_x = []
for i in x:
    if i in result_x:
        result_x.remove(i)
    else:
        result_x.append(i)

# x축과 마찬가지로 y값도 1개만 있는 값이 최종값이 된다
y = [y1, y2, y3]
result_y = []
for j in y:
    if j in result_y:
        result_y.remove(j)
    else:
        result_y.append(j)
print(*result_x, *result_y)
