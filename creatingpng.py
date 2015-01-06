import png
import numpy as np

r = ([255,0,0])
g = ([0,255,0])
b = ([0,0,255])

#Write out all elements row-wise in a single array
p = (r, g, b,   r, g, b,   r, g, b,   r, g, b) 
#Each row has a red, green and blue pixel. 4 such rows.

rows = 4
#Calculate number of columns from the number of rows specified
no_elements = len(p)
columns = no_elements/rows

#Convert 1D array to 2D array. Each pixel is 3 column wide for the three RGB channels

a = np.resize(p, (rows, 3*columns))

#numpy is row-major, while png is column-major??

f = open('hello.png', 'wb')
w = png.Writer(columns, rows)
w.write(f, a) ; f.close()