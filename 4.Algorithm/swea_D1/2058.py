#하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
number = int(input())

total = 0
while number > 1:
    total += number % 10
    number = number // 10
    
print(total)