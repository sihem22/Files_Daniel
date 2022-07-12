import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt




df = pd.read_csv('data-fusion.csv', sep = ',')
df2 = pd.read_csv('fr-fusion.csv', sep = ',')
df3 = pd.read_csv('es-fusion.csv', sep = ',')
df4 = pd.read_csv('pt-fusion.csv', sep = ',')
df5 = pd.read_csv('el-fusion.csv', sep = ',')
df6 = pd.read_csv('pl-fusion.csv', sep = ',')
df7 = pd.read_csv('ru-fusion.csv', sep = ',')
#df8 = pd.read_csv('zh-fusion.csv', sep = ',')
df9 = pd.read_csv('cn-fusion.csv', sep = ',')

print(df)
fig = plt.figure()
ax = fig.add_subplot()

x11=[x[1] for x in df.itertuples()]
y22=[y[2] for y in df.itertuples()]
x=[x[1] for x in df2.itertuples()]
y=[y[2] for y in df2.itertuples()]
x1=[x[1] for x in df3.itertuples()]
y1=[y[2] for y in df3.itertuples()]
a=[x[1] for x in df4.itertuples()]
b=[y[2] for y in df4.itertuples()]
c=[x[1] for x in df5.itertuples()]
d=[y[2] for y in df5.itertuples()]
e=[x[1] for x in df6.itertuples()]
f=[y[2] for y in df6.itertuples()]
g=[x[1] for x in df7.itertuples()]
h=[y[2] for y in df7.itertuples()]
#i=[x[1] for x in df8.itertuples()]
#j=[y[2] for y in df8.itertuples()]
k=[x[1] for x in df9.itertuples()]
l=[y[2] for y in df9.itertuples()]



ax.plot(y22, x11, color ='tab:orange')

ax.plot(y, x, color ='tab:grey',label='French')
ax.plot(y1, x1, color ='tab:purple',label='Spanish')
ax.plot(b, a, color ='tab:red',label='Portuguese')
ax.plot(d, c, color ='tab:green',label='Greek')
ax.plot(f, e,label='Russian')
ax.plot(h, g, color ='tab:pink',label='polish')
#ax.plot(j, i, color ='tab:blue',label='chinese')
ax.plot(l, k, color ='tab:brown',label='chinese')

ax.legend()
#plt.axis([0.1,0.1])
plt.xlim(0.0,1.0)
plt.ylim(0.0,1.0)



plt.plot([0,1])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.show()
