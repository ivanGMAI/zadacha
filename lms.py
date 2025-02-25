import math
import matplotlib.pyplot as plt
d = {}
with open('sp_t.txt') as f:
    f = list(f)
    f = [i.replace('\n','').split() for i in f]
    delt = float(f[0][1])
    for i in range(len(f)):
        d[int(float(f[i][1])-delt)] = round(float(f[i][0]),2)
p = open('v(t).txt','w')
high = []
tim = []
for i in range(len(d)):
    if i in [27,53,75,96,121,147,173,207]:
        continue
    else:
        high.append(d[i])
        tim.append(i)
        print(f'{i}-{d[i]}',end='\n',file=p)
p.close()
