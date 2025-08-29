def count_subtree_nodes(node, left, right):
    """노드를 루트로 하는 서브트리의 노드 개수를 세는 함수"""
    if node == 0:  # 노드가 없으면
        return 0
    
    # 현재 노드(1) + 왼쪽 서브트리 개수 + 오른쪽 서브트리 개수
    left_count = count_subtree_nodes(left[node], left, right)
    right_count = count_subtree_nodes(right[node], left, right)
    
    return 1 + left_count + right_count

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())  # E: 간선 수, N: 찾을 노드
    arr = list(map(int, input().split()))
    
    V = E + 1  # 노드 수 = 간선 수 + 1
    left = [0] * (V + 1)  
    right = [0] * (V + 1) 
    
    # 트리 구성
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:    # 왼쪽 자식이 비어있으면
            left[p] = c
        else:               # 왼쪽이 있으면 오른쪽에
            right[p] = c
    
    # N을 루트로 하는 서브트리의 노드 개수 계산
    result = count_subtree_nodes(N, left, right)
    print(f"#{tc} {result}")