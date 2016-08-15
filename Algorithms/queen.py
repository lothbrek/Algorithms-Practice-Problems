#N Queen problem

N=4
solution = [-1]*N

def Queen(i):
   if promising(i):
      if i==N-1:
         print(solution)
      else:
         for j in range(N):
            if j not in solution[0:i+1]:
               solution[i+1] = j
               Queen(i+1)

def promising(i):
   for j in range(i):
      if i-j == abs(solution[i]-solution[j]):
         return False
   return True


Queen(-1)