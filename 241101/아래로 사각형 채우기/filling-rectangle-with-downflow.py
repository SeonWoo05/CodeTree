n = int(input())

A = [[0 for _ in range(n)] for _ in range(n)]

num = 1

for i in range(n):
    for j in range(n):
        A[j][i] = num
        num += 1

for row in A:
    print(*row)