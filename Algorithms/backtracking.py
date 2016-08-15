N=4
solution = [-1]*N

# Sets(i) generates all sets from the current config solution[0..i]
def Sets(i):
   if i==N-1:
      print(solution)
   else:
      for j in range(2):
         solution[i+1] = j
         Sets(i+1)

# Generate all sets
# Sets(-1)

# Perms(i) generates all perms from the current config solution[0..i]
def Perms(i):
   if i==N-1:
      print(solution)
   else:
      for j in range(N):
         if j not in solution[0:i+1]:
            solution[i+1] = j
            Perms(i+1)

# Generate all permutations
# Perms(-1)