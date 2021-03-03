
#리스트의 모든 순열을 나열하는 과정

N = 3
card = [4, 5, 6]

for i in range(N):
    for j in range(N):
        if j != i:
            for k in range(N):
                if k != i and k != j:
                    print(card[i], card[j], card[k])
