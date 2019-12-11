
import matplotlib.pyplot as plt
from scipy import interpolate

file= open('freq', "r")
line = file.readline()
line = file.readline()
a=list()
x=list()
y=list()

i=0

while line:
    

    a.append(line)

    x.append(int((a[i].split("/")[0])))
    y.append(int((a[i].split("/")[1])))

    i+=1

    line= file.readline()
    line = file.readline()
    line= file.readline()
    line = file.readline()
file.close()

f = interpolate.interp1d(x, y)
y1 = int(f(5000)+1)
print(y1)

plt.plot(x,y)
plt.show()

