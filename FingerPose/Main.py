import os
import math

a = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]
c = [0.0, 0.0]
i = 0
lim = [1000.0, 1000.0]
dir_name = "D:\Input_2"
test = os.listdir(dir_name)
for item in test:
    str = open(dir_name + "/" + item)
    for line in str:
        line = line.rstrip().split(' ')
        a[i][0] = float(line[0])
        a[i][1] = float(line[1])
        i += 1
    i = 0

    for j in range(1, 5):
        if (lim[0] > abs(a[0][0] - a[j][0])) and (lim[1] > abs(a[0][1] - a[j][1])):
            lim[0] = abs(a[0][0] - a[j][0])
            lim[1] = abs(a[0][1] - a[j][1])

    if c[0] < lim[0]:
        c[0] = lim[0]
    if c[1] < lim[1]:
        c[1] = lim[1]

    lim[0] = 1000.0
    lim[1] = 1000.0
str.close()

c = math.sqrt(c[0]**2 + c[1]**2)
print(c)
