def sol(x, y, b, v):

    if b == 1:
        print(v)
        return

    m = b//2
    if r < x+m and c < y+m:
        sol(x, y, m, v)
    elif r < x+m and c >= y+m:
        sol(x, y+m, m, v+m**2)
    elif r >= x+m and c < y+m:
        sol(x+m, y, m, v+2*m**2)
    else:
        sol(x+m, y+m, m, v+3*m**2)

n, r, c = map(int, input().split())
sol(0, 0, 2**n, 0)

