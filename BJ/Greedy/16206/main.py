n, m = map(int, input().split())
cake10 = []; cake = []
for i in list(map(int, input().split())) :
  if i >= 10 and i % 10 == 0 : cake10 += [i]
  elif i >= 10 and i % 10 != 0 : cake += [i]
cake.sort(reverse=True);cake10.sort()

result = 0

if len(cake10) != 0 :
  for i in cake10:
    if m <= 0: break
    if m >= i // 10 - 1 : m -= (i // 10) - 1; result += i // 10
    else:result += m; m = 0

if len(cake) != 0:
  for i in cake:
    if m <= 0:break
    if m >= i // 10 : m -= (i // 10);result += i // 10
    else:result += m;m = 0

print(result)