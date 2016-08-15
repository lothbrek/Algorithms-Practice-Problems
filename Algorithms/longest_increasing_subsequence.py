Table = {}

def L(P, i):
   if i not in Table:
      m = 0
      for j in range(i):
         if (j < i) and (P[j] < P[i]):
            if m < 1+L(P, j):
               m = 1 + L(P, j)
      Table[i] = m
   return Table[i]

# return max { L(P,0), L(P,1), ...., L(P,n-1) }
def LIS(P):
   m = 1
   for i in range(1,len(P)):
      if m < L(P, i):
         m = L(P, i)
   return m

def LIS2(P):
   L = {}
   m = L[0] = 1
   for i in range(1, len(P)):
      L[i] = 1
      for j in range(i):
         if (j<i) and (P[j] < P[i]):
            if L[i] < L[j] + 1:
               L[i] = L[j] + 1
      if m < L[i]:
         m = L[i]
   return m
