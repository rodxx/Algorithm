for _ in range(int(input())):
  n, m = input().split(); cnt0 = 0; cnt1 = 0
  for i in range(len(n)):
    if int(n[i])^int(m[i]):
      if n[i] == '1':cnt1 += 1
      else:cnt0 += 1
  print(max(cnt1,cnt0))