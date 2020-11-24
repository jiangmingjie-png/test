# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:18:26 2020

@author: AI
"""
import numpy as np
import matplotlib.pyplot as plt
import re 
two_D = []
F     = []
E0    = []
x     = []
file = open('Pt_getdata.txt')
for line in file:
    getdata=re.compile(r'(0.\d{8}E\+\d\d)').findall(line)
    two_D.append(getdata)    
    print(getdata)
file.close()
for i in range(len(two_D)):
    F.append((two_D[i][0]))
    E0.append((two_D[i][1]))   
alfa=3.212620735
base=np.array([2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0])
true_alfa=base*alfa
for k in range(8):
    x.append(float(true_alfa[k]))
plt.figure()
plt.title('Pt-Simple Cubic')
plt.ylabel('E(eV)')
plt.xlabel('alfa(A)')
plt.grid()
plt.plot(x,E0,'g-1')
plt.plot(x,F,'b-2')
plt.legend('')
plt.show()