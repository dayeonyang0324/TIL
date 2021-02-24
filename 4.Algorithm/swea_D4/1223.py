# 후위 표기식으로 계산하기

def calc(N, num):
    stack_num = []
    stack_sign = []  # 숫자와 기호를 각각 stack에 넣어준다.
    total = 0
    i = 1
    stack_num.append(int(num[0]))  # 숫자가 기호보다 1개 많으므로 첫번째 항은 미리 stack에 넣어놓았다

    while i <= N//2:  # while문을 사용해서 인덱스 값을 변화시키면서 넣어주었다.
        stack_sign.append(num[2*i-1])
        stack_num.append(int(num[2*i]))

        if stack_sign.pop() == '*':  # 숫자stack과 기호stack에 하나씩 넣으면서 더하기 위에 곱셈을 쌓을 수 없으므로
            stack_num.append(stack_num.pop() * stack_num.pop())  # 곱셈이 나오면 같은 순서에 넣어준 숫자와 그전에 들어간 숫자를 pop해서 곱한다, 그러고 다시 append해줌
        i += 1  # 그러고 while문이니깐 다음 순서로 넘어가기 위해 i값을 이동해준다

    for i in range(len(stack_num)):
        total += stack_num.pop()  # stack에는 더하기로 연결된 숫자만 들어있음 (곱셈은 이미 해서 다시 stack에 쌓아놨다)

    return total  # 합 반환


T = 10
for tc in range(1, T+1):
    N = int(input())
    num = list(input())

    print('#{} {}'.format(tc, calc(N, num)))