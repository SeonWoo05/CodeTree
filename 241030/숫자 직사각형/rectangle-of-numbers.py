n,m = map(int, input().split())

A = [[0 for _ in range(m)] for _ in range(n)]

num = 1

for i in range(n):
    for j in range(m):
        A[i][j] += num
        num += 1

for row in A:
    print(*row)