n,m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if A[i][j] == B[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()