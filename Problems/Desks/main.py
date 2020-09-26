# put your python code here
import math
ans = 0
students = []

x = 0

while x < 3:
    students.append(int(input()))
    x += 1

x = 0

for x in students:
    if x % 2 != 0:
        x /= 2
        x = math.floor(x + 1)
    else:
        x /= 2

    ans += int(x)

print(ans)
