#!/bin/python
# optimize output.txt
# and do some dirty hack
b2c={}
c2b={}
cc={}
# c : chinese
# b : boshamy code

f=open("output.txt", 'r')
for l in f:
    x=l.split()
    res=x[0].decode('utf8') # result
    sol=x[1:]               # solution
    for s in sol:
        if liuDict.has_key(s):
            liuDict[s]=liuDict[s]+[res]
        else:
            liuDict[s]=[res]
f.close()
 