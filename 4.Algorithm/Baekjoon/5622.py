# 5622

word = input()

# 문자에 배당되어 있는 숫자
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# 해당 문자열이 있을때 걸리는 시간은 인덱스 +3
time = 0
for i in word:
    for j in range(len(alpha)):
        if i in alpha[j]:
            time += alpha.index(alpha[j]) + 3
print(time)
