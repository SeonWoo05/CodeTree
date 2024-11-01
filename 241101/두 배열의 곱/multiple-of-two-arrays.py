A = [list(map(int, input().split())) for i in range(3)]
blank = input()
B = [list(map(int, input().split())) for i in range(3)]

for i in range(3):
    for j in range(3):
        print(A[i][j] * B[i][j], end=" ")
    print()