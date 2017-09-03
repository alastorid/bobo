#!/bin/python
import glob

d = {}
for f in glob.glob("assets/*.txt"):
    print "processing " + f + " ..."
    fi = open(f, 'r')
    s = fi.read()
    fi.close()
    for c in s.decode('utf8'):
        if not d.has_key(c):
            d[c]=1
        else:
            d[c]=d[c]+1
    pass
    
c2b={}
b2c={}

liuTable=["liu.txt","liu_custom.txt"]
for lf in liuTable:
    f=open(lf, 'r')
    for l in f:
        x=l.split()
        res=x[0].decode('utf8') # result
        sol=x[1:]               # solution
        if c2b.has_key(res):
            c2b[res]=c2b[res]+sol
        else:
            c2b[res]=sol
        
        for s in sol:
            if b2c.has_key(s):
                b2c[s]=b2c[s]+[res]
            else:
                b2c[s]=[res]
    f.close()

f=open("output.txt",'w+')
f.write("BEGIN_TABLE\n")
for b in b2c:
    offset={}
    lm=0 # local max value
    lm2=0 # local second max value
    for c in b2c[b]:
        if d.has_key(c):
            if lm < d[c]:
                lm2=lm
                lm=d[c]

    for c in b2c[b]:
        offset[c]=0
        if not d.has_key(c): # easy fix
            d[c]=0
        # if this bcode is the only one of the char            
        if len(c2b[c])==1 and c2b[c][0]==b:
            offset[c]=lm+1
        # if b + "v" also point to c, means b is not the main bcode for this c
        if b2c.has_key(b+"V"):
            for cc in b2c[b+"V"]:
                if offset.has_key(cc):  # set it to order 2
                    if lm == d[c]:
                        offset[cc]= -d[c] + lm2 -1
                    #else:
                    #    offset[cc]= -d[c] + lm - 1 #
    for c in b2c[b]:
        #offset[c]=0
        s=("%s\t%s\t%d\n" % (b.lower(),c,offset[c]+d[c]+100))
        f.write(s.encode('utf8'))

f.write("END_TABLE\n\n")
f.close()

print "done"