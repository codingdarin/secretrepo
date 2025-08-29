def f(T):
    if T > N:

T = int(input())
for tc in range(1, T+1):

    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int(input().split()))
        tree[a] = b
    
    result = f(1)

    print(f"#{tc} {tree[T]}")


