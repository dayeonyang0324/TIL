arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

r = 1
c = 1
N = 3

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    #조건문을 달아서 넘어가면 반환되지 않도록 설정할 수 있다.
    if 0 <= nr < N and 0 <= nc < N: continue
    print(arr[nc][nr])