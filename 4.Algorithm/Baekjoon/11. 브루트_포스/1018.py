import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
table = [list(map(str, input())) for _ in range(M)]
print(table)