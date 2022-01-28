import sys
input = sys.stdin.readline

def sol(i, d):

    if i == len(s):
        r.add((''.join(d)).replace('[', '(').replace(']', ')'))
        return

    if s[i] == ')':
        k = len(d)-1
        while d[k] != '(':
            k -= 1

        t1, t2 = d[:], d[:]
        t1[k] = '['
        t1.append(']')

        t2.pop(k)
        sol(i+1, t1)
        sol(i+1, t2)

    else:
        d.append(s[i])
        sol(i+1, d)

r = set()
s = input().rstrip()
sol(0, [])
r = sorted(list(r))
print(*r[1:], sep='\n')