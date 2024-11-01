def diagonal(n,m):
    A = [[0 for _ in range(m)] for _ in range(n)]
    num = 1

    for start_col in range(m):
        row = 0
        col = start_col
        while row < n and col >= 0:
            A[row][col] = num
            num += 1
            row += 1
            col -= 1

    for start_row in range(1,n): # 열기준으로 시작하다가 다채우면 첫번째 행부터 마지막 행까지
        row = start_row
        col = m-1
        while row < n and col >= 0:
            A[row][col] = num
            num += 1
            row += 1
            col -= 1
    
    return A

n,m = map(int, input().split())
result = diagonal(n,m)

for row in result:
    print(*row)