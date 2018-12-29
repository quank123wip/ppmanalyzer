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
    for j in lstd:
        if j[0]=='#':
            continue
        if j=='P3\n' :
            continue
        elif(len(j.split())==2):
            ax,ay=j.split()
            ax=int(ax);ay=int(ay)
            outputf.write(str(ax)+' '+str(ay)+'\n')
        else:
            outputf.write(str(x)+' '+str(y)+' '+str(int(j))+'\n')
            x+=1;
            if(x==ax):
                x=0
                y+=1
        