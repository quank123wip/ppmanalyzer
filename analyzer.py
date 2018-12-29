#!/bin/env python
import os
import sys
args=sys.argv
del args[0]
if (len(args)==0) :
    print("analyzer.py Useage:analyzer.py filename.ppm")
for i in args :
    inputf=open(i,mode='r');
    outputf=open(i+".txt",mode='w')
    lstd=inputf.readlines()
    x=0;y=0
    ax=0;ay=0
    cnt=0
    while True:
        if cnt>=len(lstd):
            break
        if lstd[cnt][0]=='P':
            del lstd[cnt]
            continue
        if(len(lstd[cnt].split())==2):
            ax,ay=lstd[cnt].split()
            ax=int(ax);ay=int(ay)
            outputf.write(str(ax)+' '+str(ay)+'\n')
            del lstd[cnt]
        if lstd[cnt][0]=='#':
            del lstd[cnt]
            continue
        cnt+=1
    for i in range(0,ax):
        for j in range(0,ay):
            r=int(lstd[0]);del lstd[0]
            g=int(lstd[0]);del lstd[0]
            b=int(lstd[0]);del lstd[0]
            outputf.write(str(i)+' '+str(j)+' '+str(r)+' '+str(g)+' '+str(b)+'\n')
        