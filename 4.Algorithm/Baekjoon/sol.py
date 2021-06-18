import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    cnt = 0
    move = y - x



    """
    1
    
    11
    
    111
    121
    
    1211
    1221
    
    12211
    12221
    12321
    
    123211
    123221
    123321
    
    1233211
    1233221
    1233321
    1234321
    ...
    """


