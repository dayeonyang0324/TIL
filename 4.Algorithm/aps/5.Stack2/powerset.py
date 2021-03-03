# powerset : 부분집합 만들기

####################################

# 리스트의 부분집합
N = 3
arr = [1, 2, 3]  # 데이터
sel = [0] * N  # 해당 원소를 뽑았는지 체크

def powerset(idx):
    if idx == N:
        print(*sel)

        return

    # idx 자리 원소를 뽑고 간다.
    sel[idx] = 0
    powerset(idx + 1)

    # idx 자리 안 뽑고 간다.
    sel[idx] = 1
    powerset(idx + 1)


powerset(0)



#########################################

# def backtrack(a, k, input):
#     global MAXCANDIDATES
#     c = [0] * MAXCANDIDATES
#
#     if k == input:
#         process_solution(a, k)
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input)
#
#
# def construct_candidates(a, k, input, c):
#     c[0] = True
#     c[1] = False
#     return 2
#
#
# MAXCANDIDATES = 100
# NMAX = 100
# a = [0] * NMAX
# # a 해당원소 사용했는지 안했는지, k 인덱스, input 몇개 뽑는지
# backtrack(a, 0, 3)
