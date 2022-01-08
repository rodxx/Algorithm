def sol(o, s):

    if o == n+1:
        if eval((s.replace(" ", ""))) == 0:
            print(s)
        return

    sol(o+1, s + " " + str(o))
    sol(o+1, s + "+" + str(o))
    sol(o+1, s + "-" + str(o))

for _ in range(int(input())):
    n = int(input())
    sol(2, "1")
    print()