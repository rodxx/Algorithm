import sys
n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

first, last = 0, n-1
first_ball, last_ball = s[first], s[last]
while s[first] == first_ball and first < n-1 :
  first += 1
while s[last] == last_ball and last > 0 :
  last -= 1

# print('첫번째와 마지막 인덱스',first, last)

if first > last :
  print(0)
else:
  left_red, left_blue, right_red, right_blue = 0, 0, 0, 0
  # 빨간공 또는 파란공을 선택해서 왼쪽으로 옮기기
  for i in range(first, n):
    if s[i] == 'R':
      left_red += 1
    else:
      left_blue += 1

  # 빨간공 또는 파란공을 선택해서 오른쪽으로 옮기기
  for i in range(last+1):
    if s[i] == 'R':
      right_red += 1
    else:
      right_blue += 1

  #print(left_red, left_blue, right_red, right_blue)
  print(min(left_red, left_blue, right_red, right_blue))