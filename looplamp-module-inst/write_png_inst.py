import png
import numpy as np

inst_data = np.genfromtxt('inst_data.csv',delimiter=',', usecols = 3)

r = ([255,0,0])
g = ([0,255,0])
b = ([0,0,255])
y = ([255,255,0])


total_lights = 20
fnumber = 0;
rows = total_lights;
columns = 1;

for k, i in enumerate(inst_data):
    p = [];
    print(i)
    if (i == 1):
        p.append(g)
    if (i == 2):
        p.append(b)
    if (i == 3):
        p.append(y)
    if (i == 4):
        p.append(r)

    print(p)

    a = np.resize(p, (rows, 3*columns))

    f = open('inst%03d.png' % k, 'wb')
    w = png.Writer(columns, rows)
    w.write(f, a) ; f.close()
