dim = [5,2,3,4,6,7,8]
# dim[i] is equal to col[i] or row[i+1]

N = len(dim)

def M(i, j):
	if i==j:
		return 0
	m = M(i,i) + M(i+1,j) + dim[i-1]*dim[i]*dim[j]
	for k in range(i,j):
		if m > M(i,k) + M(k+1,j) + dim[i-1]*dim[k]*dim[j]:
			m = M(i,k) + M(k+1,j) + dim[i-1]*dim[k]*dim[j]
	return m

print("Minimum number of multiplications:", M(1,N-1))