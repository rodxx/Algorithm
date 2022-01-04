import sys
input = sys.stdin.readline

def check(x):

    for i in range(x):
        if row[i] == row[x]:
            return False
        if abs(row[i] - row[x]) == x-i:
            return False

    return True

def sol(x):

    if x == n:
        global r
        r += 1
        return

    for i in range(n):
        row[x] = i
        if check(x):
            sol(x+1)


n = int(input())
row = [0]*n
r = 0
sol(0)
print(r)