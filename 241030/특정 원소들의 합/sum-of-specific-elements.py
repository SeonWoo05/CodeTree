A = []

for i in range(4):
    B = list(map(int, input().split()))
    A.append(B)

C = 0
for j in range(4):
    for k in range(j+1):
        C += A[j][k]

print(C)