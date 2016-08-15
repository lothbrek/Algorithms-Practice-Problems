#dynamic programmign implementation of optimal matrix multiplication
dim = [5,2,3,4,6,7,8]
dim = [10,4,5,20,2,50,39,2,20,35,54,7,8,59,3,58,9,3]
# dim[i] is equal to col[i] or row[i+1]

N = len(dim)

# initialize matrix
M = [0] * N
P = [-1] * N

for i in range(N):
	M[i] = [0]*N
	P[i] = [-1]*N

# compute M
for i in reversed(range(1,N)):
	for j in range(i+1,N):
		# M[i][j] = M[i][k] + M[k+1][j] + row[i] * col[i] * col[j]
		M[i][j] = M[i][i] + M[i+1][j] + dim[i-1]*dim[i]*dim[j]
		P[i][j] = i
		for k in range(i,j):
			if M[i][j] > M[i][k] + M[k+1][j] + dim[i-1]*dim[k]*dim[j]:
				M[i][j] = M[i][k] + M[k+1][j] + dim[i-1]*dim[k]*dim[j]
				P[i][j] = k


def Order(i, j):
	if i==j:
		print("A"+str(i), end=" ")
	else:
		k = P[i][j]
		print("(", end=" ")
		Order(i, k)
		Order(k+1, j)
		print(")", end=" ")

print("Minimum number of multiplications:", M[1][N-1])
Order(1,6)
print()