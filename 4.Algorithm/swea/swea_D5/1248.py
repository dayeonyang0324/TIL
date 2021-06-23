# subtree의 갯수를 구하는 함수
def subtree_size(n):
    global cnt
    for i in tree[n]:
        cnt += 1
        subtree_size(i)


T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    num_list = list(map(int, input().split()))
    tree = [[] for _ in range(V + 1)]
    parent = [0] * (V + 1)
    cnt = 1

    # 부모 노드에 자식 노드 추가
    for i in range(0, 2 * E, 2):
        parent[num_list[i+1]] = num_list[i]
        tree[num_list[i]].append(num_list[i + 1])

    n1_result = []  # n1이 지나는 노드들을 아래부터 위로 리스트에 담기
    n2_result = []  # n2도 똑같이 리스트에 담기
    while n1 != n2:
        n1 = parent[n1]
        n1_result.append(n1)
        n2 = parent[n2]
        n2_result.append(n2)

    # n1, n2가 지나가는 모든 노드들이 리스트에 담기고 여기에서 중복되는 가장 큰 값을 선택한다
    result = []
    for i in range(len(n1_result)):
        for j in range(len(n2_result)):
            if n1_result[i] == n2_result[j]:
                result.append(n1_result[i])
                break

    # 가장 큰 값을 선택한게 겹치는 노드가 되고, 겹치는 노드의 subtree크기를 구할 수 있다.
    subtree_size(result[0])
    print('#{} {} {}'.format(tc, result[0], cnt))