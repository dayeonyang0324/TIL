# 3053

from math import pi

N = int(input())
# 유클리드 원의 넓이 = pi * r^2
euclid = (N ** 2) * pi
# 택시 기하학 원의 넓이 = 2 * r * r
taxi = 2 * N * N

# 소숫점 6자리까지 나타내기 위해 format사용, round는 부동소숫점이 표현되지 않음
print('{:.6f}'.format(euclid))
print('{:.6f}'.format(taxi))
