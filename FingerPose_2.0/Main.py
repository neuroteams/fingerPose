import os
import math

const = 17.43
a = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]
c = 0
i = 0
cycl = 0
output = [0, 0, 0, 0]
lim = [1000.0, 1000.0]
dir_name = "D:\Input_3"
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

    c = math.sqrt(lim[0]**2 + lim[1]**2)

    if c <= const and lim[0] == abs(a[0][0] - a[1][0]):
        #print('Указательный')
        output[0] = 1
    elif c <= const and lim[0] == abs(a[0][0] - a[2][0]):
        #print('Средний')
        output[1] = 1
    elif c <= const and lim[0] == abs(a[0][0] - a[3][0]):
        #print('Безымянный')
        output[2] = 1
    elif c <= const and lim[0] == abs(a[0][0] - a[4][0]):
        #print('Мизинец')
        output[3] = 1
        if [1, 1, 1, 1] == output:
            cycl += 1
            output = [0, 0, 0, 0]

    lim[0] = 1000.0
    lim[1] = 1000.0
str.close()

print(cycl)
