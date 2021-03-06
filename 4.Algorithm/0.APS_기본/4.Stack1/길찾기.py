# 경로 만들기
# 1. dictionary
g1 = {
    'A':['D', 'C'],
    'B':['C', 'E'],
    'C':[],
    'D':['F'],
    'E':[],
    'F':[]
}


# 2. Adj list
g2 = [
    [],  # 0
    [4, 3],  # 1
    [3, 5],  # 2
    [],  # 3
    [6],  # 4
    [],  # 5
    [],  # 6
]

# 시작점 = 값_리스트의[인덱스]
# 도착점 = 값_리스트의[인덱스]
# 그래프[시작점].append(도착점)


# 3. Adj matrix
g3 = [
    ['T', 'F', 'F', 'F'],
    ['F', 'T', 'T', 'F'],
    ['F', 'T', 'F', 'T'],
    ['F', 'F', 'T', 'T']
]
