import png
import numpy as np

#budget_data = np.genfromtxt('budget_data.csv',delimiter=',', usecols = 1)
budget_data = range(20,-5,-1)

r = ([255,0,0])
g = ([0,255,0])
b = ([0,0,255])

p1 = []
total_lights = 20
fnumber = 0;
rows = total_lights;
columns = 1;

for k,i in enumerate(budget_data):
    p = [];
    print i
    if (i > 0):
        for j in range(total_lights):
            if (j < i):
                p.append(g)
            else: 
                p.append(b)
    else:
        for j in range(total_lights):
            if (j >= np.abs(i)):
                p.append(b)
            else:
                p.append(r)
                
    print p
    
    a = np.resize(p, (rows, 3*columns))
   
    f = open('budget%03d.png' % k, 'wb')
    w = png.Writer(columns, rows)
    w.write(f, a) ; f.close()
    
    
    
