A = list(input()); B = list(input())
tmp1 = A[:];tmp2 = B[:];state=True
tmp1.sort(); tmp2.sort()
n = len(A)
for i in range(n):
  if tmp1[i] != tmp2[i]:state=False

count = 0
i, j = n-1, n-1

while i >= 0 and j >= 0:
  if B[i] == A[j]:
    count += 1
    i -= 1
    j -= 1
  else: j -= 1
if state:print(n - count)
else:print(-1)