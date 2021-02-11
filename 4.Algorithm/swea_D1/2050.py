#알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.


#예시코드가 알파벳 순서로 이뤄져 있어서 순서대로 인덱스를 추출하는 방식을 생각했다.
#alph = list(input())

#total = []
#for i in range(len(alph)):
#    total.append(i+1)
#print(*total)


#그러나 문제에서'알파벳으로 이뤄진 문자열'을 보고 아스키 코드로 풀어야하는 문제였다,,
alpha = list(input())
for i in range(len(alpha)):
    print(ord(alpha[i])-64, end=' ')