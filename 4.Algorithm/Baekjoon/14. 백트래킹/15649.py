# 15649

# N, M = map(int, input().split())
#
# result = []
# def back():
#     # 조건을 만족한다면 탈출
#     if len(result) == M:
#         print(*result)
#         return
#
#     # 모든 수를 다 돌면서 조건에 만족한다면 리스트 넣기
#     for i in range(1, N+1):
#         if i not in result:
#             result.append(i)
#             # 다음 애들을 재귀로 확인한다. 조건 만족하면 탈출 아니라면 꺼내고 다시 반복
#             back()
#             result.pop()
#
# back()


# 다른 풀이
N, M = map(int, input().split())
visit = [False] * N  # 방문 확인
result = []  # 결과 목록 리스트

def back(lenr, N, M):
    if lenr == M:  # 조건 만족하면 함수 탈출
        print(*result)
        return

    for i in range(N):
        if not visit[i]:  # 방문하지 않았다면
            visit[i] = True  # 방문표시 하고
            result.append(i+1)  # 결과값에 값 넣기
            back(lenr+1, N, M)  # 나머지는 재귀로 다시 돌려넣기
            visit[i] = False  # 방문 취소하고
            result.pop()  # 뽑기

back(0, N, M)  # 길이 시작은 0부터
