# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:18:26 2020

@author: AI
"""
import numpy as np
import matplotlib.pyplot as plt
import re 
def getdatalist(datafile):        #the text of compile is ('-.XXXXXXX') 
    two_D = []
    F     = []
    E0    = []
    file = open(datafile)
    for line in file:
        getdata=re.compile(r'(-.\d{8}E\+\d\d)').findall(line)  #change in proper time
        two_D.append(getdata)
    file.close()
    for i in range(len(two_D)):
        F.append(float(two_D[i][0]))                #the importance of this step!!!
        E0.append(float(two_D[i][1]))
    return F,E0
    #F:getdatalist[0]
    #E0:getdatalist[1]
def draw_a_E(datafile,a,b,d):
    F = getdatalist(datafile)[1]
    X = np.arange(a,b+1,d)    #the range of X (a,b)
    plt.figure()
    plt.title('Pt-Simple Cubic')
    plt.ylabel('E(eV)')
    plt.xlabel('a/$\dot A $')
    plt.plot(X,F,'r-1')
    plt.show()
    
'''  
F_SCP = getdatalist('data_SCP.txt')[1]
F_HCP1 = getdatalist('data_HCP1.txt')[1]
F_HCP7 = getdatalist('data_HCP7.txt')[1]
F_Hf = getdatalist('data_Hf.txt')[0]
F_ScAl = getdatalist('data_ScAl.txt')[1]
F_NaCl = getdatalist('data_NaCl.txt')[1]
X1 = np.arange(2.30,3.01,0.05)
X2 = np.arange(3.35,4.31,0.05)
X3 = np.arange(2.70,3.21,0.05)
X4 = np.arange(2.70,4.21,0.05)
X5 = np.arange(3.00,4.01,0.05)
#z1=np.polyfit(X,F,2)
#p1=np.poly1d(z1)
plt.figure()
plt.title('Pt-Simple Cubic')
plt.ylabel('E(eV)')
plt.xlabel('a/$\dot A $')
#plt.ylim((-4.0,-2.30))
#plt.plot(X1,F_SCP,'g-1',label='SCP')
#plt.plot(X3,F_HCP1,'b-2',label='HCP:c/a=1.6')
#plt.plot(X3,F_HCP7,'r-3',label='HCP:c/a=1.78')
#plt.plot(X5,F_ScAl,'b-3',label = 'AcAl')
#plt.plot(X5,F_NaCl,'g-1',label = 'NaCl')
#plt.plot(X,F_FCP,'b-2',label='FCP')
plt.legend()
plt.show()'''