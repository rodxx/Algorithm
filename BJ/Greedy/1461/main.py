import sys
from bisect import bisect_right
input = sys.stdin.readline

def cal(a):
    result = a[-1]
    if len(a) > m:
        i = m
        while i < len(a):
            result += 2 * a[-1-i]
            i += m
    return result

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
zero = bisect_right(s, 0)
l, r = sorted(list((map(lambda x: -x, s[:zero])))), s[zero:]

# print(l,r,sep='\n')

ans = 0
if len(r) > 0:
    ans += cal(r)
if len(l) > 0:
    ans += cal(l)
if len(r) > 0 and len(l) > 0:
    ans += min(r[-1], l[-1])
print(ans)