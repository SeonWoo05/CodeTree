n = int(input())

A = [[0 for _ in range(n)] for _ in range(n)]

num = n*n
for i in range(n):
    if n % 2 == 0: 
        if i % 2 == 0:
            for j in range(n-1,-1,-1):
                A[j][i] = num
                num -= 1
        else:
            for j in range(n):
                A[j][i] = num
                num -= 1
    else:
        if i % 2 == 0:
            for j in range(n):
                A[j][i] = num
                num -= 1
            for j in range(n-1,-1,-1):
                A[j][i] = num
                num -= 1
        else:
            for j in range(n-1,-1,-1):
                A[j][i] = num
                num -= 1
                
for row in A:
    print(*row)