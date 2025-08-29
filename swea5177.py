def enq(n):
    global last
    # 마지막 정점 추가: 완전 이진 트리 유지를 위해
    last += 1
    heap[last] = n
    c = last # 새로 추가된 자식 노드의 인덱스
    p = last // 2  # 완전 이진트리의 부모 노드 인덱스

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0

    for i in arr:
        enq(i)

    p = last // 2
    ans = 0

    while p:
        ans += heap[p]
        p //= 2


    print(f"#{tc} {ans}")
