import sys
input = sys.stdin.readline
n = int(input()); cnt = 0
if (n % 5) % 2 == 0:cnt += n // 5 + (n % 5) //2
else:cnt += n//5 - 1 + (n%5 + 5) // 2
if n < 5 and n%2 != 0 : print(-1)
else: print(cnt)