#!/bin/env python
import os
import sys
args=sys.argv
del args[0]
if (len(args)==0) :
    print("analyzer.py Usage:analyzer.py filename.ppm")
intBuffer=[]
def InitintBuffer(filename):
    intBuffer.clear()
    f=open(filename,"r")
    while True:
        cache=f.readline()
        if cache=='':
            break
        if cache[0]=='P':
            continue;
        for i in range(0,len(cache)):
            if cache[i]=='#':
                cache=cache[0:i]
                break
        intcache=cache.split()
        for i in intcache:
            intBuffer.append(int(i))
    f.close()# Important!
def Buffer_Getint():
    p=intBuffer[0]
    del intBuffer[0]
    return p
def Convert(filename):
    outfile_name='todo_'+filename+'.list'
    InitintBuffer(filename)
    outf=open(outfile_name,'w')
    mx=Buffer_Getint();my=Buffer_Getint();
    outf.write(str(mx)+' '+str(my)+'\n')
    Buffer_Getint()
    for i in range(0,mx):
        for j in range(0,my):
            outf.write(str(i)+' '+str(j)+' '+str(Buffer_Getint())+' '+str(Buffer_Getint())+' '+str(Buffer_Getint())+'\n')
    outf.close()
for arg in args:
    Convert(arg)
