#knapsack with bound computed based on greedy algorithm
W = [2,5,10,5]
V = [40,30,50,10]
C = 16
N = len(W)
solution, best_solution, best_value = [-1]*N, None, 0

def Knapsack(i, cur_w, cur_v):
   global best_value, best_solution
   if promising(i, cur_w, cur_v):
      print(solution[0:i+1])
      if i==N-1:
         if best_value < cur_v:
            best_solution, best_value = list(solution), cur_v
      else:
         solution[i+1] = 0
         Knapsack(i+1, cur_w, cur_v)
         solution[i+1] = 1
         Knapsack(i+1, cur_w+W[i+1], cur_v+V[i+1])

def promising(i, cur_w, cur_v):
   if cur_w > C: return False
   total_w, bound = cur_w, cur_v
   j = i+1
   while j<=N-1 and total_w+W[j] <= C:
      total_w += W[j]
      bound += V[j]
      j += 1
   if j<=N-1:
      bound += V[j] * (C-total_w) / float(W[j])
   if bound > best_value: return True
   return False

Knapsack(-1, 0, 0)
print("BEST:",best_value, best_solution)