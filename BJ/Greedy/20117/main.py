n = int(input());s = sorted(list(map(int,input().split())))
if n % 2 == 0: print(2 * sum(s[n//2:]))
else: print(2*sum(s[n//2:]) - s[n//2])