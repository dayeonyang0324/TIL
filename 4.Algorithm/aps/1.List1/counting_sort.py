
#카운팅 정렬은 정수에만 적용 가능하다.
#list에서 (가장 큰 값 + 1) 크기의 count리스트를 만든다.
#count = [0] * (N)

def Counting_sort(A, B, k):
    #A[] #입력배열
    #B[] #정렬된 배열
    #C[] #카운트 배열

    C = [0] * k

    for i in range(0, len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i+1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1



