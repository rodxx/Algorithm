import sys
input = sys.stdin.readline
string = input().rstrip()
string = string.replace('XXXX','AAAA')
string = string.replace('XX','BB')
if 'X' in string:print(-1)
else: print(string)