#입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.
#for문을 사용하지 않고 풀 수 있다.
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[N // 2])