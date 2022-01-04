import sys
input = sys.stdin.readline

def sol(a, b, p, d):

    if len(d) == l:
        if a > 0 and b > 1:
            print(d)
        return

    for i in range(p, c):
        if s[i] in v:
            sol(a+1, b, i+1, d+s[i])
        else:
            sol(a, b+1, i+1, d+s[i])


l, c = map(int, input().split())
s = sorted(list(input().split()))
v = ['i', 'e', 'a', 'o', 'u']
sol(0, 0, 0, "")