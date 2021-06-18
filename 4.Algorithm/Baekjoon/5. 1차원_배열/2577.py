# 2577

# count 내장 함수 사용하기 위해 str 로 만들어야 함
num = list(input() for _ in range(3))
new_num = str(int(num[0]) * int(num[1]) * int(num[2]))
# 하나하나 출력할 수 있고
# print(new_num.count('0'))
# print(new_num.count('1'))
# print(new_num.count('2'))
# print(new_num.count('3'))
# print(new_num.count('4'))
# print(new_num.count('5'))
# print(new_num.count('6'))
# print(new_num.count('7'))
# print(new_num.count('8'))
# print(new_num.count('9'))


# for 문과 f-string 사용해서 출력할 수 있음
for i in range(10):
    print(new_num.count(f'{i}'))
